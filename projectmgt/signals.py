from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import *
from authentication.models import User
from django.core.mail import send_mail
from django.utils.html import strip_tags
import decimal
from authentication.models import *

@receiver(m2m_changed, sender=Invoice.invoices.through)
def update_invoice_total_amount(sender, instance, action, **kwargs):
    if action == 'post_add':
        amount = decimal.Decimal(0.00)

        for invoice_item in instance.invoices.all():
            amount += decimal.Decimal(invoice_item.quantity) * decimal.Decimal(invoice_item.amount)

        instance.amount = amount
        instance.save(update_fields=['amount'])
        # print(f"Signal triggered for Invoice ID: {instance.id}")



@receiver(post_save, sender=Project)
def notify_user_on_project_creation(sender, instance, created, **kwargs):
    if created and instance.client_email and instance.client_name:
        # Check if the email is associated with an existing user
        existing_user = User.objects.filter(email=instance.client_email).exists()

        if not existing_user:
            # Create a user account
            username = instance.client_name
            email = instance.client_email
            password = f"{instance.client_name.lower().replace(' ', '')}123"
            roles = Role.objects.get_or_create(name='client')

            # Create a User instance
            user = User.objects.create_user(username=username, email=email, password=password, roles=roles)
            print(f"User account created for {username}")

            # Send account details to the client via email
            html_message = f"""
               <html>
            <head>
                <style>
                    /* Define CSS styles for the email */
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                        margin: 0;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 30px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    .message {{
                        font-size: 16px;
                        line-height: 1.6;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007bff;
                        color: #fff;
                        text-decoration: none;
                        border-radius: 5px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Welcome, {instance.client_name}!</h2>
                    <p class="message">
                        Your account has been created successfully. Here are your login details:<br>
                        <strong>Email:</strong> {instance.client_email}<br>
                        <strong>Password:</strong> {password}<br><br>
                        <a href="https://outlined-projects.vercel.app" class="btn">Login to Your Account</a> 
                        <br><br>
                        (If the button doesn't work, copy and paste this link in your browser: 
                        <a href="https://outlined-projects.vercel.app">https://outlined-projects.vercel.app</a>)
                    </p>
                </div>
            </body>
        </html>
            """

            # Send HTML email
            send_mail(
                'Account Created Successfully',
                strip_tags(html_message),  # Remove HTML tags for plain text fallback
                'from@example.com',
                [instance.client_email],
                html_message=html_message,  # Include the HTML content
                fail_silently=False,
            )
            print(f"Email sent to {instance.client_email} with account details")
        else:
            # Notify the user that the email is already in use
            print(f"Email {instance.client_email} is already associated with another user. Not sending account creation email.")

@receiver(post_save, sender=Project)
def send_project_details(sender, instance, created, **kwargs):
    if created:
        # Extract necessary project details
        project_name = instance.name
        project_description = instance.description
        project_location = instance.location
        project_start_date = instance.start_date
        project_end_date = instance.end_date
        project_supervisor = instance.supervisor.username if instance.supervisor else "Not assigned"
        project_architect = instance.architect.username if instance.architect else "Not assigned"
        # Add other necessary project details...

        # Compose the email message with project details
        html_message = f"""
        <html>
            <head>
                <style>
                    /* Define CSS styles for the email */
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                        margin: 0;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 30px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    h2 {{
                        color: #007bff;
                    }}
                    ul {{
                        list-style-type: none;
                        padding-left: 0;
                    }}
                    li {{
                        margin-bottom: 10px;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #007bff;
                        color: #fff;
                        text-decoration: none;
                        border-radius: 5px;
                    }}
                    .btn:hover {{
                        background-color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Hello {instance.client_name}!</h2>
                    <p>Your new project '{project_name}' has been created successfully.</p>
                    <p>Project Details:</p>
                    <ul>
                        <li><strong>Name:</strong> {project_name}</li>
                        <li><strong>Description:</strong> {project_description}</li>
                        <li><strong>Location:</strong> {project_location}</li>
                        <li><strong>Start Date:</strong> {project_start_date}</li>
                        <li><strong>End Date:</strong> {project_end_date}</li>
                        <li><strong>Supervisor:</strong> {project_supervisor}</li>
                        <li><strong>Architect:</strong> {project_architect}</li>
                        <!-- Add other project details here -->
                    </ul>
                    <p>You can log in to our platform to view and manage your project.</p>
                    <a href="https://outlined-projects.vercel.app" class="btn">Login to Your Account</a>
                    <br><br>
                    (If the button doesn't work, copy and paste this link in your browser:
                    <a href="https://outlined-projects.vercel.app">https://outlined-projects.vercel.app</a>)
                    <p>Thank you for choosing Outline Designs!</p>
                </div>
            </body>
        </html>
        """

        # Send email with project details to the client
        send_mail(
            'A New Project,{instance.name}, was created successfully',
            strip_tags(html_message),  # Remove HTML tags for plain text fallback
            'from@example.com',
            [instance.client_email],
            html_message=html_message,  # Include the HTML content
            fail_silently=False,
        )
# @receiver(post_save, sender=Invoice)
# def send_invoice_email(sender, instance, created, **kwargs):
#     if created:
#         # Calculate the total amount of invoice items
#         total_amount = sum(item.amount * item.quantity for item in instance.invoices.all())

#         # Compose the email message
#         subject = 'New Invoice Created'
#         html_message = f"""
#             <html>
#                 <head>
#                     <style>
#                         /* Define CSS styles for the email */
#                         /* ... (styles remain the same) ... */
#                     </style>
#                 </head>
#                 <body>
#                     <div class="container">
#                         <h2>Hello {instance.name}!</h2>
#                         <p>A new invoice has been created for your project.</p>
#                         <p>Invoice Items:</p>
#                         <ul>
#                             <!-- Loop through and list invoice items -->
#                             {% for item in instance.invoices.all %}
#                                 <li>{item.quantity} x {item.content} - ${item.amount * item.quantity}</li>
#                             {% endfor %}
#                         </ul>
#                         <p><strong>Total Amount:</strong> ${total_amount}</p>
#                         <!-- Add more details as needed -->
#                         <p>Thank you!</p>
#                     </div>
#                 </body>
#             </html>
#         """
#         from_email = 'from@example.com'
#         recipient_list = [instance.email]  # Assuming email is related to the user instance

#         # Send the HTML email
#         send_mail(
#             subject,
#             strip_tags(html_message),  # Remove HTML tags for plain text fallback
#             from_email,
#             recipient_list,
#             html_message=html_message,  # Include the HTML content
#             fail_silently=False,
#         )

@receiver(post_save, sender=Todo)
def update_spendings(sender, instance, created, **kwargs):
    if created or any(
        field in kwargs['update_fields'] 
        for field in ['company_earnings', 'labour', 'facilitation']
    ):
        # Assuming 'company_earnings', 'labour', 'facilitation' are DecimalField in Task model
        # Calculate spendings based on these fields
        spendings = instance.company_earnings + instance.labour + instance.facilitation
        instance.spendings = spendings
        instance.save(update_fields=['spendings'])
