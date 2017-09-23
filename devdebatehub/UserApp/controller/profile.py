from django.shortcuts import render, get_object_or_404
from django.contrib import auth as permissionauth
from UserApp.models import User,Person,Organisation,FollowingUser,UserActivity,Story
from devdebate.models import Blog,Debate
from UserApp.forms import PersonRegistration,EditProfile,MessageForm
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
import simplejson as json
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect


# local user controllers
def personeditprofilepage():
	return {
	'form1'		: PersonRegistration(),
	'highlight' : "border-bottom: 2px solid #4caf50;" }

def personupdatedetailspage(user_name, request):
	person 		= get_object_or_404(User, username = user_name)
	instance 	= get_object_or_404(Person, user = person)
	return {
	'form1'		: EditProfile(instance = instance),
	'highlight' : "border-bottom: 2px solid #4caf50;" }

	

def personfunc(user_name, request):
	personname 			= get_object_or_404(User, username = user_name)
	persondetails 		= get_object_or_404(Person, user = personname)
	following_followers = get_object_or_404(FollowingUser, person = personname)
	cannotfollow 		= False
	activities			= personname.activity_of.all()
	for i in following_followers.followers.all():
		if i == request.user:
			cannotfollow = True
			break

	print(activities)
	return {
	'person' 		: personname,
	'persondetails'	: persondetails,
	'highlight' 	: "border-bottom: 2px solid #4caf50;",
	'following' 	: following_followers.following.all().count(),
	'followers'		: following_followers.followers.all().count(),
	'cannotfollow' 	: cannotfollow,
	'activities'	: activities
	 }

def profileinfo(request, user_name):
	account = get_object_or_404(User, username = user_name)
	if account.usertype is None:
		context = personfunc(user_name, request)
		# extracontext = personupdatedetailspage()
		# context = {**context, **extracontext}
		return render(request, 'UserApp/person/ProfileInfo.html', context)
	else:
		context = organisationfunc(user_name)
		return render(request, 'UserApp/org/Profileorg.html', context)

def message(request, user_name):
	context = {}
	account = get_object_or_404(User, username = user_name)
	if account.usertype is None:
		context = personfunc(user_name, request)
		context['form']	= MessageForm()
		context['highlight'] = "border-bottom: 2px solid #4caf50;"
		return render(request, 'UserApp/person/message.html', context)
	else:
		context = organisationfunc(user_name)
		return render(request, 'UserApp/org/Profileorg.html', context)

def editprofileperson(request, user_name):
	userinstance = get_object_or_404(User, username = user_name)
	if request.user == userinstance:
		context = {}
		account = get_object_or_404(User, username = user_name)
		if account.usertype is None:
			context 		= personfunc(user_name, request)
			extracontext 	= personeditprofilepage()
			context 		= {**context, **extracontext}
			return render(request, 'UserApp/person/editprofile.html', context)
		else:
			context = organisationfunc(user_name)
			return render(request, 'UserApp/org/Profileorg.html', context)
	else:
		raise Http404

def updateperson(request, user_name):
	userinstance = get_object_or_404(User, username = user_name)
	if request.user == userinstance:
		context = {}
		account = get_object_or_404(User, username = user_name)
		if account.usertype is None:
			context 		= personfunc(user_name, request)
			extracontext 	= personupdatedetailspage(user_name, request)
			context 		= {**context, **extracontext}
			return render(request, 'UserApp/person/updateperson.html', context)
		else:
			context = organisationfunc(user_name)
			return render(request, 'UserApp/org/Profileorg.html', context)
	else:
		raise Http404

# ajax update controller
def updatepersondetails(request, user_name):
	person = request.user
	instance = get_object_or_404(Person, user = person)
	update = True
	if request.method == 'POST':
		form = EditProfile(data = request.POST, files = request.FILES, instance = instance)
		if form.is_valid():
			print(True, form)
			obj = form.save(commit = False)
			print(obj)
			obj.user = request.user
			obj.save()
			print("---------------------------------------------")
			print(obj)
			return JsonResponse(
            json.dumps({ 'updated' : update }),
            content_type="application/json",
            safe =False
        )
# ajax update controller
def updateuser(request, user_name):
	instance 	= request.user
	context		= {}
	updated		= True
	try:
		dob = request.POST.get('dob')
		instance.dob = dob
	except:
		pass

	try:
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 == password2:
			instance.set_password(password1)
		else:
			updated = False
	except:
		pass

	instance.save()

	if updated:
		user = authenticate(username=request.user.email , password = password1)
		login(request,user)

	return JsonResponse(
            json.dumps({ 'updated' : updated }),
            content_type="application/json",
            safe 		=False
        )
# homepage for any user
def profilepage(request, user_name):
	context = {}
	account = get_object_or_404(User, username = user_name)
	if account.usertype == None:
		context = personfunc(user_name, request)
		return render(request, 'UserApp/person/Profile.html', context)
	else:
		context = organisationfunc(user_name, request)
		return render(request, 'UserApp/org/Profileorg.html', context)

def blog(request, user_name):
	context = {}
	blogcontext	= {}
	account = get_object_or_404(User, username = user_name)
	if account.usertype is None:
		context 	= personfunc(request, user_name)
		return render(request, 'UserApp/person/Profile.html', context)
	else:
		context = organisationfunc(user_name, request)
		blogcontext	= blogfunc(request, user_name)
		context 	= { **context, **blogcontext }
		return render(request, 'UserApp/org/Profileorgblog.html', context)

def blogfunc(request, user_name):
	context = {}
	user_instance 		= get_object_or_404(User, username = user_name)
	context['blogs']	= user_instance.blog_written_by.all()
	return context

def debatehosted(request, user_name):
	context = {}
	blogcontext	= {}
	account = get_object_or_404(User, username = user_name)
	if account.usertype is None:
		context 	= personfunc(request, user_name)
		return render(request, 'UserApp/person/Profile.html', context)
	else:
		context = organisationfunc(user_name, request)
		debatecontext	= debatelisted(request, user_name)
		context 	= { **context, **debatecontext }
		return render(request, 'UserApp/org/debatehosted.html', context)

def debatelisted(request, user_name):
	print("okhy")
	context = {}
	user_instance = get_object_or_404(User, username = user_name)
	context['debatelist'] = user_instance.hosted_by.all()
	return context


def organisationfunc(user_name, request):
	context 			= {}
	user_instance 		= get_object_or_404(User, username = user_name)
	org_instance		= get_object_or_404(Organisation, user = user_instance)
	following_followers = get_object_or_404(FollowingUser, person = user_instance)
	cannotfollow		= False
	for i in following_followers.followers.all():
		if i == request.user:
			cannotfollow = True
			break
	context['org']		= user_instance
	context['orgdetails']	= org_instance
	context['highlight']	= "border-bottom: 2px solid #4caf50;"
	context['stories']		=  user_instance.story_by.all()
	context['cannotfollow']	= cannotfollow
	context['following']	= following_followers.following.all().count()
	context['followers']	= following_followers.followers.all().count()
	return context

def logout(request, user_name):
	permissionauth.logout(request)
	return HttpResponseRedirect('/')
