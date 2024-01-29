
from celery import shared_task
from Email_campaign_manager.celery import app
import smtplib, os
from django.core.mail import EmailMessage, get_connection

@shared_task
def send_email(message) :
    html_message = open('email.html', 'r').read()
    html = replace_text(html_message)
    msg = EmailMessage(subject, html, email_from,recipient_list, connection=connection) 
    msg.content_subtype = 'text/html'
    msg.send()
    


def replace_text(html, message) :
    id = message['id']
    name = message['name']
    email = message['email']
    content = message['content']
    html = html.replace("{{ id }}", str(id))
    html = html.replace("{{ name }}", name)
    html = html.replace("{{ email }}", email)
    html = html.replace("{{ content }}", content)
    return html