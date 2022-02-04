from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


# LEarn about different model fields


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=False, null=True, max_length=140, db_index=True
    )
    image = CloudinaryField(
        "Image", blank=True
    )

    like = models.IntegerField(
        "Like", blank=True, null=False, default=0  
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    
