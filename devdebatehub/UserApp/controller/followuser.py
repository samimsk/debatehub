from django.shortcuts import render, get_object_or_404
from UserApp.models import User,Person,Organisation,FollowingUser,UserActivity
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
import simplejson as json

@login_required
def follow(request, user_name):
	follower 	= request.user
	following   =  get_object_or_404(User, username = user_name)
	followers_instance 	= get_object_or_404(FollowingUser, person = follower)
	followers_instance.following.add(following)
	followers_instance.save()
	followings_instance	= get_object_or_404(FollowingUser, person = following) 
	followings_instance.followers.add(follower)
	followings_instance.save()
	context = {}
	context["success"] = True
	return JsonResponse(
            json.dumps(context),
            content_type="application/json",
            safe=False
        )

