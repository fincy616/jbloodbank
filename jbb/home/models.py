from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from random import choices
from statistics import mode
from sys import maxsize
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.forms import ModelChoiceField



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Enter a valid Email ID.")
        email= self.normalize_email(email)

        user= self.model(
            email = email,
            **extra_fields
        )

        print(password)
        print(email)
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    uid = models.AutoField(
        primary_key=True,
    )
    full_name = models.CharField(
        max_length= 50,
        verbose_name= 'Full Name',
        blank= False,
        null= False,
    )

    email = models.EmailField(
        verbose_name= 'Email ID',
        unique= True,
        null= False,
        blank= False,
        help_text= "Please enter your college Email ID."
    )

    address = models.TextField(
        verbose_name= 'Address',
        blank= False,
        null= False,
    )

    height = models.FloatField(
        verbose_name= 'Height',
        null=True,
        blank= True,
        help_text= 'Please enter your height in CM.',
    )

    weight = models.FloatField(
        verbose_name= 'Weight',
        null=True,
        blank= True,
        help_text="Enter your weight in Kilogram.",
    )
    phn_no = models.IntegerField(
        verbose_name= 'Phone Number',
        null= True,
        blank= True,
    )

    pincode = models.IntegerField(
        verbose_name= 'Pincode',
        null= True,
        blank= True,
    )

    blood_group = models.CharField(
        max_length= 3,
        choices = [('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-')],
        default = 'A+'
    )

    gender = models.CharField(
        max_length= 6,
        choices= [('female','Female'),('male','Male'),('others','Others')],
        default= 'others',
    )
    # prof_pic = models.ImageField(
    #     upload_to = 'users',
    #  )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        # full_name
    ]
    objects = UserManager()
    
    # list_filters = ('blood_group','pincode','gender')
    def __str__(self):
        return self.full_name

class Blood_Request(models.Model):
    p_name= models.CharField(
         max_length= 20,
        #  default='patient'
    )
    p_bloodneed = models.TextField()
    p_gender= models.CharField(
        max_length = 10,
        choices= [('female','Female'),('male','Male'),('others','Others')],
        default= 'others',
    )
    # p_pincode = models.IntegerField()
    p_hospitalname = models.TextField()
    p_bystander = models.TextField()
    p_phn_number = models.IntegerField()
    p_bloodgroup = models.CharField(
        max_length= 3,
        choices = [('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('B-','B-'),('O-','O-'),('AB-','AB-')],
        default = 'A+'
    )

    p_unit = models.SmallIntegerField()
    # p_email = models.EmailField()
    p_reqstudent = models.ForeignKey(User, on_delete=models.CASCADE,
    null=True,
    blank=True,
    )
    
class email_id(models.Model):
    mail_id = models.EmailField()

    def __str__(self):
        return self.mail_id
    
