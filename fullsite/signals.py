from authentication import models
from django.dispatch import receiver
from fullsite import models
from django.db.models.signals import post_save

@receiver(post_save,sender=models.User)
def makeCart(sender, instance ,created,**kwargs):
    if(created):
        models.Cart(user=instance).save()
