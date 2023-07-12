from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Tag(models.Model):
    label=models.CharField(max_length=40)

class TagItems(models.Model):
    # what tag applied to what object
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    # to define a generic relationship these 3 steps are necessary.
    # give variable names like this only.
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()
    
