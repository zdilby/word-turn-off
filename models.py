from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

# Create your models here.
class Words(models.Model):
    level = models.IntegerField(_('level'),blank=True,null=True)
    classify = models.CharField(_('classify'),max_length=32,blank=True,null=True)
    title = models.CharField(_('title'),max_length=64)
    features = models.TextField(_('features'),max_length=256,blank=True,null=True)

class WordsSet(models.Model):
    pernum = models.IntegerField(_('pernum'),blank=True,null=True)
    orderby = models.CharField(_('orderby'),max_length=64,blank=True,null=True)
    cur_cla = models.CharField(_('current classify'),max_length=32,blank=True,null=True)

