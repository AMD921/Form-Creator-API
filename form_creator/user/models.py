from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    is_private = models.BooleanField(default=True)  # پیشفرض فرم‌ها و داده‌های کاربر خصوصی است
    email_verified = models.BooleanField(default=False)  # وضعیت تأیید ایمیل

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username

# تابعی برای اضافه کردن کاربر جدید به گروه پیش‌فرض
@receiver(post_save, sender=CustomUser)
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        default_group, _ = Group.objects.get_or_create(name='default_group')
        instance.groups.add(default_group)
