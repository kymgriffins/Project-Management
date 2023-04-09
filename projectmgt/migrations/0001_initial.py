# Generated by Django 4.1.7 on 2023-04-09 14:15

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Blueprints')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('work_planned', models.TextField(blank=True, max_length=500)),
                ('issues', models.TextField(blank=True, max_length=500)),
                ('workers_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_spendings', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_achieved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RecordPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Blueprints')),
                ('daily_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.dailyrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('foundation', 'Foundation'), ('framing', 'Framing'), ('rough-in', 'Rough-In'), ('finishing', 'Finishing'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('on-hold', 'On Hold')], max_length=255)),
                ('current_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estimated_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('architect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='architect_projects', to=settings.AUTH_USER_MODEL)),
                ('blueprints', models.ManyToManyField(blank=True, related_name='blueprints', to='projectmgt.blueprint')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('foreman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreman_projects', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervised_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_used', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.dailyrecord')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.material')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.invoice')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.material')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoices',
            field=models.ManyToManyField(related_name='invoices', to='projectmgt.invoiceitem'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.project'),
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='records', to='projectmgt.recordpics'),
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, related_name='materials', to='projectmgt.materialusage'),
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.project'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('daily_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.dailyrecord')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floors', models.IntegerField()),
                ('square_feet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='projectmgt.project')),
            ],
        ),
        migrations.AddField(
            model_name='blueprint',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmgt.project'),
        ),
    ]
