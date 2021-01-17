from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bedrijfsnaam = models.CharField(max_length=300,blank=True)
    omschrijving = models.TextField(max_length=500,blank=True)
    contactpersoon = models.CharField(max_length=200, blank=True)
    straatnaam = models.CharField(max_length=300, blank=True)
    postcode = models.CharField(max_length=7, blank=True)
    plaats = models.CharField(max_length=100, blank=True)
    telefoonnummer = models.CharField(max_length=15, blank=True)
    website = models.URLField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='logos',blank=True)
    foto = models.ImageField(upload_to='fotos',blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




#from wagtail.core.models import Page
#from wagtail.core.fields import RichTextField
#from wagtail.admin.edit_handlers import FieldPanel
#from wagtail.search import index

"""
class LedenLijst(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class LedenProfiel(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
"""
