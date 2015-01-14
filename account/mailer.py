# -*- coding: utf-8 -*-

from django.core.mail import EmailMessage
from django.template import loader

from settings import EMAIL_HOST_USER

def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, EMAIL_HOST_recipient_list)
    msg.content_subtype = "html"
    msg.send()








