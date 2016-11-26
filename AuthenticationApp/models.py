"""AuthenticationApp Models

Created by Naman Patwari on 10/4/2016.
"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from ProjectsApp.models import Project

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email=None, uname=None, password=None, first_name=None, last_name=None,
    		is_student=None, is_professor=None, is_engineer=None, bookmarks=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not uname:
            raise ValueError('Users must have a uname')
        #We can safetly create the user
        #Only the email field is required
        user = self.model(email=email, uname=uname, first_name=first_name, last_name=last_name, bookmarks=bookmarks)
        user.set_password(password)

        #If first_name is not present, set it as email's username by default
        if first_name is None or first_name == "" or first_name == '':                                
            user.first_name = email[:email.find("@")]            
        #Classify the Users as Students, Professors, Engineers
        if is_student == True and is_professor == True and is_engineer == True:
        	#hack to set Admin using forms
        	user.is_admin = True
       	elif is_student == True:
       		user.is_student = True
       	elif is_professor == True:
       		user.is_professor = True
       	elif is_engineer == True:
       		user.is_engineer = True
       	else:
       		user.is_admin = True
        
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, uname=None, password=None, first_name=None, last_name=None, bookmarks=None):
        user = self.create_user(email, uname, password=password, first_name=first_name, last_name=last_name,
        	is_student=None, is_professor=None, is_engineer=None, bookmarks = bookmarks)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_student(self, email=None, uname=None, password=None,first_name=None, last_name=None, bookmarks=None):
        return self.create_user(email, uname, password=password,first_name=first_name, last_name=last_name,
    	is_student=True, is_professor=False, is_engineer=False, bookmarks=bookmarks)

    def create_professor(self, email=None, uname=None, password=None,first_name=None, last_name=None, bookmarks=None):
        return self.create_user(email, uname, password=password,first_name=first_name, last_name=last_name,
    	is_student=False, is_professor=True, is_engineer=False, bookmarks=bookmarks)

    def create_engineer(self, email=None, uname=None, password=None,first_name=None, last_name=None, bookmarks=None):
        return self.create_user(email, uname, password=password,first_name=first_name, last_name=last_name,
    	is_student=False, is_professor=False, is_engineer=True, bookmarks=bookmarks)


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    uname = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
    	max_length=120,
    	null=True,
    	blank=True,
    	)    

    last_name = models.CharField(
    	max_length=120,
    	null=True,
    	blank=True,
    	)

    is_active = models.BooleanField(default=True,)
    is_admin = models.BooleanField(default=False,)

    #New fields added
    is_student = models.BooleanField(default=False,)
    is_professor = models.BooleanField(default=False,)
    is_engineer = models.BooleanField(default=False,)    

    bookmarks = models.ManyToManyField(Project)
        

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):        
        return "%s %s" %(self.first_name, self.last_name)

    def get_short_name(self):        
        return self.first_name

    def get_uname(self):
        return self.uname

    def __str__(self):              #Python 3
        return self.email

    def __unicode__(self):           # Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):        
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
#     def new_user_reciever(sender, instance, created, *args, **kwargs):
#     	if created:   
     
# Going to use signals to send emails
# post_save.connect(new_user_reciever, sender=MyUser)
             

