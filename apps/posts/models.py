from pdb import post_mortem
from django.db import models

# models
from ..users.models import User

# Create your models here

class Posts(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,null=False, blank=False)
    description = models.CharField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    # picture = models.ForeignKey(Camera,on_delete=models.CASCADE,null=True,blank=True)
    # file = models.ForeignKey(Files,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'
    


