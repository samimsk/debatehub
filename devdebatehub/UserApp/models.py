from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils import timezone
from UserApp.choices import *
from devdebate.models import *
import os

def get_person_pic_path(instance, filename):
    return os.path.join('person_photos', str(instance.id), filename)
def get_org_pic_path(instance, filename):
    return os.path.join('org_photos', str(instance.id), filename)

# base class of Person and Organisation
class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField( unique=True, blank = False)
    username 	= models.CharField(unique = True, max_length = 30, blank = True)
    usertype    = models.CharField(choices = USER_TYPE_CHOICES, blank = True, max_length = 50, null = True)
    dob         = models.CharField(blank = True, null = True, max_length = 100)
    is_active 	= models.BooleanField( default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    paricipation= models.IntegerField( default = 0)

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural ='users'

    def get_full_name(self):
        # will be overridden in subclasses
        pass

    def get_short_name(self):
        # will be overridden in subclasses
        pass


class Person(models.Model):
    user            = models.OneToOneField(User,on_delete = models.CASCADE, related_name = "person")
    firstname       = models.CharField(max_length = 30, blank = True, null = True)
    lastname        = models.CharField(max_length = 30, blank = True, null = True)
    details         = models.CharField(max_length = 500, blank = True, null = True)
    location        = models.CharField(max_length = 30, blank = True, null = True)
    works_at        = models.CharField(max_length = 30, blank = True, null = True)
    memberat        = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "memberof", null = True),
    collage         = models.CharField(max_length = 30, blank = True, null = True)
    interestedin    = models.CharField(max_length = 100, blank = True, null = True)
    memberof        = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "memberof", null = True),
    profileimage    = models.ImageField(upload_to=get_person_pic_path, blank= True, null= True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural ='persons'

    def __str__(self):
        return self.user.username


class Organisation(models.Model):
    user                = models.OneToOneField(User,on_delete = models.CASCADE, related_name = "organisation")
    name                = models.CharField(max_length = 100, blank = True)
    photo               = models.ImageField(upload_to =get_org_pic_path, blank= True, null= True)
    location            = models.CharField(max_length = 100, blank = True)
    details             = models.CharField(max_length = 500, blank = True)

    class Meta:
        verbose_name = 'org'
        verbose_name_plural ='orgs'

    def __str__(self):
        return self.user.username


class FollowingUser(models.Model):
    person          = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followingfollowers")
    following       = models.ManyToManyField(User, related_name = 'following', blank = True, null = True)
    followers       = models.ManyToManyField(User, related_name = 'followers', blank = True, null = True)

    def __str__(self):
        return self.person.username


class UserActivity(models.Model):
    person          = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "activity_of")
    opinion         = models.ForeignKey(Opinion, blank = True, null = True)

    def __str__(self):
        return " User Activity List of  " + self.person.username    

class Message(models.Model):
    sender      = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "sender")
    receiver    = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "receiver")
    message     = models.CharField(max_length = 100, blank = False)


class Story(models.Model):
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "story_by")
    heading   = models.CharField(max_length = 100, blank = False)
    body      = models.CharField(max_length = 200, blank = False)
