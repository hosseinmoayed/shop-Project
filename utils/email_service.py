from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
def send_email(subject , to , context , templatename):
    try:
        html_message = render_to_string(template_name=templatename , context=context)
        message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject ,message=message , from_email= from_email , recipient_list=[to] , html_message=html_message)
    except Exception as e:
        print(e)
