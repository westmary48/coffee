from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .shops import Shop


class Barista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Shop,
        null=True,
        blank=True,
        on_delete=models.CASCADE)


# These receiver hooks allow you to continue to
# work with the `User` class in your Python code.


# Every time a `User` is created, a matching `Barista`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_barista(sender, instance, created, **kwargs):
    if created:
        Barista.objects.create(user=instance)

# Every time a `User` is saved, its matching `Barista`
# object will be saved.
@receiver(post_save, sender=User)
def save_barista(sender, instance, **kwargs):
    instance.barista.save()