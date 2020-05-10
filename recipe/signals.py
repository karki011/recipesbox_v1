from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Author
from django.contrib.auth.models import Group


def author_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='author')
        instance.groups.add(group)
        Author.objects.create(
            user=instance,
            name=instance.username
        )

        print('Author profile created!')


post_save.connect(author_profile, sender=User)
