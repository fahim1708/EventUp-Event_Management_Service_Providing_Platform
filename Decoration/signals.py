from django.db.models.signals import post_delete, post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Item, Package, Package_Detail, Profile


MEDIA_MODELS = (Item, Package, Package_Detail, Profile)


def delete_file(field_file):
    if field_file and field_file.name:
        field_file.delete(save=False)


@receiver(pre_save)
def remove_replaced_media(sender, instance, **kwargs):
    if sender not in MEDIA_MODELS or not instance.pk:
        return

    try:
        previous = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    fields = {
        Item: ('Cover_Image',),
        Package: ('image',),
        Package_Detail: ('file',),
        Profile: ('profile_picture',),
    }[sender]
    for field_name in fields:
        old_file = getattr(previous, field_name)
        new_file = getattr(instance, field_name)
        if old_file.name and old_file.name != new_file.name:
            delete_file(old_file)


@receiver(post_delete)
def remove_deleted_media(sender, instance, **kwargs):
    if sender not in MEDIA_MODELS:
        return

    fields = {
        Item: ('Cover_Image',),
        Package: ('image',),
        Package_Detail: ('file',),
        Profile: ('profile_picture',),
    }[sender]
    for field_name in fields:
        delete_file(getattr(instance, field_name))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

