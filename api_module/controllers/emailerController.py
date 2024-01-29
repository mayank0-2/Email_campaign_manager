
from celery import shared_task
from Email_campaign_manager.celery import app
import smtplib, os
from django.core.mail import EmailMessage, get_connection

@shared_task
def send_email() :
    html_message = open('email.html', 'r')
    msg = EmailMessage(subject, html_message, email_from,recipient_list, connection=connection) 
    msg.content_subtype = 'text/html'
    msg.send()
    