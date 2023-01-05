from celery import shared_task

from .models import CustomUser

@shared_task(bind=True)
def celery_send_mail(request, user_id, subject, message):
    user = CustomUser.objects.get(pk = user_id)
    user.email_user(subject=subject, message=message)
    return None