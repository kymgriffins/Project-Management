from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import *
from authentication.models import User

from django.core.mail import send_mail
from django.utils.html import strip_tags

@receiver(post_save, sender=User)
def send_user_creation_email(sender, instance, created, **kwargs):
    if created:
        # Compose the email message with HTML styling
        subject = 'Account Created Successfully'
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
                    <h2>Welcome, {instance.username}!</h2>
                    <p class="message">
                        Your account has been created successfully.<br>
                        <a href="https://outlined-projects.vercel.app" class="btn">Login to Your Account</a> 
                        <br><br>
                        (If the button doesn't work, copy and paste this link in your browser: 
                        <a href="https://outlined-projects.vercel.app">https://outlined-projects.vercel.app</a>)
                        <br>

                        Welcome aboard Developer! <br>


                    </p>
                </div>
               
            </body>
        </html>
        """
        from_email = 'from@example.com'
        recipient_list = [instance.email]

        # Send the HTML email
        send_mail(
            subject,
            strip_tags(html_message),  # Remove HTML tags for plain text fallback
            from_email,
            recipient_list,
            html_message=html_message,  # Include the HTML content
            fail_silently=False,
        )
