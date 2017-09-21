from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import simplejson as json
from UserApp.models import User,Organisation,Person,FollowingUser
from UserApp.forms import *



def auth(request):
	email = request.POST.get('email' , '')
	password = request.POST.get('password', '')
	user = authenticate(username=email , password = password)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/user/login/errorlogin')

def registrationpage(request):
    return render(request,'UserApp/registerorg.html', { 'form1' : OrgRegistration() })

def register_person(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        response_data = {}
        response_data['success'] = True
        print("hello world")
        if User.objects.filter(email=email).exists():
        	response_data['emailvailidation']	= 'Email id already exist'
        	response_data['success'] = False
        if User.objects.filter(username=username).exists():
        	response_data['usernamevailidation']	= 'Username is taken'
        	response_data['success'] = False
        if password1 != password2:
        	response_data['passwordmismatch']	= 'Password do not match'
        	response_data['success'] = False

        if response_data['success'] == True:
            user = User.objects.create_user(email = email, username = username, password = password1)
            user.save()
            
            newperson = Person.objects.create(user = user)
            newperson.save()
            followingfollowers = FollowingUser.objects.create(person = user)
            followingfollowers.save()

        return JsonResponse(
            json.dumps(response_data),
            content_type="application/json",
            safe=False
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json",
            safe =False
        )

def register_org(request):
    if request.method == 'POST':
        email       = request.POST.get('email')
        username    = request.POST.get('username')
        password1   = request.POST.get('password1')
        password2   = request.POST.get('password2')
        usertype    = request.POST.get('usertype')
        dob         = request.POST.get('dob')

        response_data = {}
        response_data['success'] = True
        print("hello cruel world")
        print(email)

        if User.objects.filter(email=email).exists():
            response_data['emailvailidation']   = 'Email id already exist'
            response_data['success'] = False
        if User.objects.filter(username=username).exists():
            response_data['usernamevailidation']    = 'Username is taken'
            response_data['success'] = False
        if password1 != password2:
            response_data['passwordmismatch']   = 'Password do not match'
            response_data['success'] = False
        if usertype != "university" and usertype != "school" and usertype != "companies" and usertype != "media"and usertype != "ngo":
            response_data['usertypeerror']   = 'Select a usertype'
            response_data['success'] = False
        if response_data['success'] == True:
            user = User.objects.create_user(
                email = email, 
                username = username, 
                password = password1,
                )
            user.usertype = usertype
            user.dob = dob
            user.save()

            orgdetails = Organisation.objects.create(user = user)
            orgdetails.save()
            
        return JsonResponse(
            json.dumps(response_data),
            content_type="application/json",
            safe=False
        )
    else:
        return JsonResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json",
            safe =False
        )

def loginuser(request):
    args = {}
    return render(request, 'UserApp/login.html', args)
 