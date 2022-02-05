# Django
from django.db import models

# user model
from apps.posts.models import Posts

# Camera model
class Camera(models.Model):
    
    #fields
    id = models.AutoField(primary_key=True)
    date_of_picture = models.DateField(auto_now_add=True,blank=None,null=None)
    picture = models.ImageField(upload_to='pictures',null=False)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return f'Picture {self.id}'