# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from Social.models import Like, Comment
from payments.models import Payment
from .models import Follow, Notification


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,
            notification_type='like',
            text=f'{instance.user.username} liked your post.'
        )


@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.followed,
            notification_type='follow',
            text=f'{instance.follower.username} followed you.'
        )


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,
            notification_type='comment',
            text=f'{instance.user.username} commented on your post: "{instance.text}".'
        )


@receiver(post_save, sender=Payment)
def create_payment_notification(sender, instance, created, **kwargs):
    if created:
        text = f"Payment received for course: {instance.course}"
        Notification.objects.create(
            user=instance.user,
            notification_type='payment',
            text=text
        )