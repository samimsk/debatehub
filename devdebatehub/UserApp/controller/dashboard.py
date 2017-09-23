from django.shortcuts import render, get_object_or_404
from UserApp.forms import EditOrgDetails,OrgRegistration,DebateForm,BlogForm,StoryForm
from UserApp.models import User,Organisation
from django.contrib.auth import authenticate,login
from django.http import Http404

def dashboard(request, user_name):
	context = {}
	context['form'] = OrgRegistration(instance = request.user)
	context['background'] = "rgba(221, 221, 221, 0.7);"
	if request.user.usertype != None:
		return render(request, "UserApp/org/dashboard.html", context)
	else:
		raise Http404()

def editcredentials(request, user_name):
	context			= {}
	usertype		= request.POST.get('usertype', '')
	username 	 	= request.POST.get('username', '')
	password 		= request.POST.get('password2', '')
	try:
		user_instance 	= User.objects.get(username = username)
		if user_instance == request.user:
			context['error']= 'Your have enterd your old username!'
		else:
			context['error']= 'Your username id is taken or invalid!'

	except:
		userpermission = authenticate(username=request.user.email , password = password)
		if userpermission != None:
			request.user.username = username
			request.user.usertype = usertype
			request.user.save()
			context['message'] = "You have updated your credentials"
		else:
			context['passworderror'] = "Wrong password entered!"

	return render(request, 'UserApp/org/saved.html', context)

def editorgdetails(request, user_name):
	context = {}
	instance = get_object_or_404(Organisation, user = request.user)
	context['form'] = EditOrgDetails(instance = instance)
	return render(request, 'UserApp/org/edit_details.html', context)
	if request.user.usertype != None:
		return render(request, 'UserApp/org/edit_details.html', context)
	else:
		raise Http404()


def updateorgdetails(request, user_name):
	context = {}
	if request.method == 'POST':
		instance = get_object_or_404(Organisation, user = request.user)
		form = EditOrgDetails(data = request.POST, files = request.FILES, instance = instance)
		if form.is_valid():
			print('true')
			obj = form.save(commit = False)
			obj.save()
			context['message'] = "Your details are saved successfully"
			return render(request, 'UserApp/org/saved.html', context)

def createdebatepage(request, user_name):
	if request.user.usertype != None:
		return render(request, 'UserApp/org/createdebate.html', {'form': DebateForm() })
	else:
		raise Http404()

def createdebate(request, user_name):
	context ={}
	if request.method == 'POST':
		form = DebateForm(data = request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.hostedby =  request.user
			obj.save()
			context['message'] = "You have added a new debate."
			return render(request, 'UserApp/org/saved.html', context)
		else:
			context['Error creating debate']
			return render(request, 'UserApp/org/saved.html', context)

def createblogpage(request, user_name):
	if request.user.usertype != None:
		return render(request, 'UserApp/org/create_blog.html', {'form': BlogForm() })
	else:
		raise Http404()

def createblog(request, user_name):
	context ={}
	if request.method == 'POST':
		form = BlogForm(data = request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.writtenby =  request.user
			obj.save()
			context['message'] = "You have added a new blog."
			return render(request, 'UserApp/org/saved.html', context)
		else:
			context['Error creating blog']
			return render(request, 'UserApp/org/saved.html', context)

def createstoriespage(request, user_name):
	if request.user.usertype != None:
		return render(request, 'UserApp/org/create_stories.html', {'form': StoryForm() })
	else:
		raise Http404()

def createstories(request, user_name):
	context ={}
	if request.method == 'POST':
		form = StoryForm(data = request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.posted_by =  request.user
			obj.save()
			context['message'] = "You have added a story."
			return render(request, 'UserApp/org/saved.html', context)
		else:
			context['Error creating blog']
			return render(request, 'UserApp/org/saved.html', context)
