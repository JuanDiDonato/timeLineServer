from django.db import models

# user model
from apps.users.models import User

# model to upload files and videos

class Files(models.Model):

    # fields
    id = models.AutoField(primary_key=True)
    date_of_file = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='files',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    
    def __str__(self):
        return f'File {self.id}'