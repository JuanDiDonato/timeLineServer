# DJango
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField

# User
class UserManager(BaseUserManager):
    
    def create_user(self,email,username,password):
        # Create new user
        if not email:
            raise ValueError('Complete todos los campos.')
        
        email = self.normalize_email(email)
        user = self.model(email=email,username=username)
        user.set_password(password)  # Encrypt password
        user.save(using=self._db)
        return user
    
    # Create new superuser
    def create_superuser(self,email,username,password):
        user = self.create_user(email,username,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

# User model.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255,unique=True,null=False,blank=False)
    username = models.CharField(max_length=255,null=False,blank=False,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta :
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Formato de visualizacion
    def __str__(self):
        return f'Usuario: {self.username}'
