# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.template import loader

from django.conf import settings
# from settings import EMAIL_HOST_USER    # 项目配置邮件地址
# from django.conf.settings import EMAIL_HOST_USER


def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, settings.EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html"
    msg.send()


def send_email():
    subject = "邮件主题"
    html_content = '<p>This is an <strong>important</strong> message.</p>'

    ''''
    html_content = loader.render_to_string(
        template_path,          # 需要渲染的html模板
        {
            'paramters': paramters  # 参数
        }
    )
    '''
    send_html_mail(subject, html_content, ['929679459@qq.com', '1658000644@qq.com'])
