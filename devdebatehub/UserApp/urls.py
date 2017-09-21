from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from UserApp.controller.authandregview import *
from UserApp.controller.profile import *
from UserApp.controller.followuser import *
from UserApp.controller.dashboard import dashboard,editcredentials, editorgdetails,updateorgdetails,createdebatepage,createdebate,createblogpage,createblog, createstories, createstoriespage

urlpatterns = [
    url(r'^person-registration/$', register_person, name = 'register_person'),
    url(r'^org-registration/$', register_org, name = 'register_org'),
    url(r'^registration/organisation/$', registrationpage, name = 'registration_page'),
    url(r'^auth/$', auth, name = 'auth'),
   	url(r'^login/errorlogin$', loginuser, name = 'login'),
    url(r'^(?P<user_name>\w+)/logout/$', logout, name = 'logout'),
    url(r'^(?P<user_name>\w+)/$', profilepage, name = 'profile'),
    url(r'^(?P<user_name>\w+)/profileinfo/$', profileinfo, name = 'profileinfo'),
    url(r'^(?P<user_name>\w+)/editprofileperson/$', editprofileperson, name = 'edit_profile_person'),
    url(r'^updateuser/$', updateuser, name = 'update_user'),
    url(r'^(?P<user_name>\w+)/updateperson/$', updateperson, name = 'update_person'),
    url(r'^updatepersondetails/$', updatepersondetails, name = 'update_person_details'),
    url(r'^(?P<user_name>\w+)/follow/$', follow, name = 'follow_user'),
    url(r'^(?P<user_name>\w+)/message/$', message, name = 'message_user'),
    url(r'^(?P<user_name>\w+)/blogs/$', blog, name = 'blog'),
    url(r'^(?P<user_name>\w+)/debatehosted/$', debatehosted, name = 'debatehosted'),
    url(r'^(?P<user_name>\w+)/dashboard/$', dashboard, name = 'dashboard'),
    url(r'^(?P<user_name>\w+)/editcredentials/$', editcredentials, name = 'editcredentials'),
    url(r'^(?P<user_name>\w+)/editorgdetails/$', editorgdetails, name = 'editorgdetails'),
    url(r'^(?P<user_name>\w+)/updateorgdetails/$', updateorgdetails, name = 'updateorgdetails'),
    url(r'^(?P<user_name>\w+)/createdebatepage/$', createdebatepage, name = 'createdebatepage'),
    url(r'^(?P<user_name>\w+)/createdebate/$', createdebate, name = 'createdebate'),
    url(r'^(?P<user_name>\w+)/createblogpage/$', createblogpage, name = 'createblogpage'),
    url(r'^(?P<user_name>\w+)/createblog/$', createblog, name = 'createblog'),
    url(r'^(?P<user_name>\w+)/createstoriespage/$', createstoriespage, name = 'createstoriespage'),
    url(r'^(?P<user_name>\w+)/createstories/$', createstories, name = 'createstories'),


]