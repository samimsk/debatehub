from django import forms 
from UserApp.models import *
from django.contrib.auth.forms import UserCreationForm
from UserApp.choices import USER_TYPE_CHOICES
from django.contrib.admin.widgets import AdminDateWidget
from UserApp.models import Person,Organisation,Message,Story
from devdebate.models import Debate,Blog

class PersonRegistration(UserCreationForm):
    password1   = forms.CharField(widget=forms.PasswordInput(
        attrs = {
        'id'            : 'passwordfield1', 
        'placeholder'   : 'password',
        'class'         : 'form-control bordr' }))
    password2   = forms.CharField(widget=forms.PasswordInput(
        attrs = {
        'id'            : 'passwordfield2', 
        'placeholder'   : ' re - password',
        'class'         : 'form-control bordr' }))
    
    class Meta:
        model 	= User
        fields 	= ('email', 'username', 'password1', 'password2', 'dob')
        widgets = {
            'email': forms.EmailInput(
                attrs={ 
                'id'            : 'emailfield',
                'class'         : 'form-control bordr',
                'placeholder'   : 'email',
                'rows'          : '1',
                }),
            'username'  : forms.Textarea(
                attrs={
                'id'            : 'usernamefield',
                'class'         : 'form-control bordr',
                'placeholder'   : 'username',
                'rows'          : '1',
                'required'      : 'True'
                }),
            'dob': forms.Textarea(
                attrs={ 
                'id'            : 'dob',
                'class'         : 'form-control bordr',
                'placeholder'   : 'dd/mm/yy',
                'rows'          : '1',
                }),

        }
class OrgRegistration(PersonRegistration):
    dob         = forms.DateField(widget=AdminDateWidget)
    usertype   = forms.ChoiceField(choices = USER_TYPE_CHOICES, widget=forms.Select(
        attrs = {
        'id'            : 'usertypefieldorg', 
        'placeholder'   : ' Select type of user',
        'class'         : 'form-control bordr' }))

    class Meta:
        model  = User
        fields  = ('email', 'username', 'dob', 'usertype', 'password1', 'password2' )
        widgets = {
            'email': forms.EmailInput(
                attrs={ 
                'id'            : 'emailfieldorg',
                'class'         : 'form-control bordr',
                'placeholder'   : 'email',
                'rows'          : '1',
                }),
            'username'  : forms.Textarea(
                attrs={
                'id'            : 'usernamefieldorg',
                'class'         : 'form-control bordr',
                'placeholder'   : 'username',
                'rows'          : '1',
                'required'      : 'True'
                }),

        }
class EditOrgDetails(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = {'name', 'photo', 'location', 'details'}
        widgets = {
            'name': forms.Textarea(
                attrs={ 
                'id'            : 'name',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Name',
                'rows'          : '1',
                }),
            'location'  : forms.Textarea(
                attrs={
                'id'            : 'location',
                'class'         : 'form-control bordr',
                'placeholder'   : 'location',
                'rows'          : '1',
                }),
            'details'  : forms.Textarea(
                attrs={
                'id'            : 'details',
                'class'         : 'form-control bordr',
                'placeholder'   : 'details',
                'rows'          : '8',
                }),
            }
            
class EditProfile(forms.ModelForm):
    class Meta:
        model   = Person
        fields  = {'firstname', 'lastname', 'details', 'location', 'works_at', 'collage', 'interestedin', 'profileimage'}
        widgets = {
            'firstname': forms.Textarea(
                attrs={ 
                'id'            : 'firstname',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Firstname',
                'rows'          : '1',
                }),
            'lastname'  : forms.Textarea(
                attrs={
                'id'            : 'lastname',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Lastname',
                'rows'          : '1',
                }),
            'details'  : forms.Textarea(
                attrs={
                'id'            : 'details',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Your intro',
                'rows'          : '8',
                }),
            'location'  : forms.Textarea(
                attrs={
                'id'            : 'location',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Where do you live?',
                'rows'          : '1',
                }),
            'works_at'  : forms.Textarea(
                attrs={
                'id'            : 'works_at',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Workplace',
                'rows'          : '1',
                }),
            'collage'  : forms.Textarea(
                attrs={
                'id'            : 'collage',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Collage',
                'rows'          : '1',
                }),
            'interestedin'  : forms.Textarea(
                attrs={
                'id'            : 'interestedin',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Your interests?',
                'rows'          : '8',
                }),

        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields  = {'message'}
        widgets = {
            'message'  : forms.Textarea(
                attrs={
                'id'            : 'message',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write a message',
                'rows'          : '8',
                }),
            }

class DebateForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields  = {'title', 'description',}
        widgets = {
            'title'  : forms.Textarea(
                attrs={
                'id'            : 'title',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write a topic heading',
                'rows'          : '2',
                }),
            'description'  : forms.Textarea(
                attrs={
                'id'            : 'description',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write a desciption',
                'rows'          : '8',
                }),
            }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields  = {'heading', 'description',}
        widgets = {
            'heading'  : forms.Textarea(
                attrs={
                'id'            : 'heading',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write blog topic',
                'rows'          : '1',
                }),
            'description'  : forms.Textarea(
                attrs={
                'id'            : 'description',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write a desciption',
                'rows'          : '15',
                }),
            }
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields  = {'heading', 'body',}
        widgets = {
            'heading'  : forms.Textarea(
                attrs={
                'id'            : 'heading',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write heading for the stories',
                'rows'          : '1',
                }),
            'body'  : forms.Textarea(
                attrs={
                'id'            : 'body',
                'class'         : 'form-control bordr',
                'placeholder'   : 'Write a desciption',
                'rows'          : '15',
                }),
            }


















    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     self.instance.username = self.cleaned_data.get('username')
    #     password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
    #     return password2

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     # checking for duplicate using and operator
    #     if email and User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('You have already registered')
    #     return email

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     # checking for duplicate using and operator
    #     if username and User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Username is alrady taken. Type a new one.')
    #     return username




# class PersonRegistration(forms.ModelForm):
# 	class meta:
# 		model 	= User
# 		fields 	= ('email', 'username', 'usertype', 'dob', 'password', 'password2')

# 	def clean(self):
# 		form_data = self.cleaned_data

