from django.shortcuts import render, get_object_or_404
from UserApp.forms import OrgRegistration,PersonRegistration
from devdebate.models import Debate,Opinion,OpinionRating,ForAgainst
from UserApp.models import Story
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import simplejson as json
from django.shortcuts import redirect
from devdebate.forms import OpinionForm


def home(request):
	args = {}
	if request.user.is_authenticated():
		args["homefeedlist"] = Debate.objects.all()
		return render(request, 'devdebate/feedhome.html', args)
	else:
		form = OrgRegistration()
		args['form1'] = form
		return render(request, 'devdebate/home.html', args)

@login_required
def feedstories(request):
	args = {}
	args["storyfeed"] = Story.objects.all()
	return render(request, 'devdebate/feedstories.html', args)

def debatedetail(request, debate_id):
	args 		= {}
	debate 		= get_object_or_404(Debate, pk = debate_id)
	opinionfor 	= debate.topic_opinion.filter(fororagainst = True).count()
	opinionlist = debate.topic_opinion.all().count()
	if opinionlist == 0:
		opinionlist = 1
	status = int((opinionfor/opinionlist)*100)

	try:
		ForAgainst.objects.get(name = request.user, topic = debate)
		showsupport = False
	except:
		showsupport = True
	args['showsupport'] = showsupport
	args['supporter']	= ForAgainst.objects.filter(topic = debate).count()
	args['debate'] 		= debate
	args['opinions']	= debate.topic_opinion.all()
	args['status']		= status
	args['form']		= OpinionForm()
	args['opinionscount']= debate.topic_opinion.all().count()
	print("okhy")
	return render(request, 'devdebate/debatedetail.html',args)

def votefor(request, debate_id):
	args = {}
	debate_instance = get_object_or_404(Debate, pk = debate_id)
	vote = ForAgainst.objects.create(topic = debate_instance, name = request.user)
	vote.save()
	args["showunvotefor"] 	= True
	args["supporter"]		= ForAgainst.objects.filter(topic = debate_instance ).count()
	return JsonResponse(
            json.dumps(args),
            content_type="application/json",
            safe=False
        )

def unvotefor(request, debate_id):
	args = {}
	debate_instance = get_object_or_404(Debate, pk = debate_id)
	unvote = ForAgainst.objects.get(topic = debate_instance, name = request.user)
	unvote.delete()
	args["showvotefor"] = True
	args["supporter"]	= ForAgainst.objects.filter(topic = debate_instance).count()
	return JsonResponse(
            json.dumps(args),
            content_type="application/json",
            safe=False
        )

def legit(request, debate_id, opinion_id):
	args = {}
	debate_instance = get_object_or_404(Debate, pk = debate_id)
	opinion_instance = get_object_or_404(Opinion, pk = opinion_id)
	opinion_instance.legit += 1
	opinion_instance.save()
	args["legitcount"] = opinion_instance.legit
	return JsonResponse(
            json.dumps(args),
            content_type="application/json",
            safe=False
        )

def submitopinion(request,debate_id):
	debate_instance = get_object_or_404(Debate, pk = debate_id)
	debate_instance.opinioncount = debate_instance.topic_opinion.all().count()
	debate_instance.save()
	args = {}
	if request.method == "POST":
		form = OpinionForm(data = request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.topic = debate_instance
			obj.opinionby = request.user
			print(request.POST.get('fororagainst'));
			if request.POST.get('fororagainst') == 'against' :
				obj.fororagainst = False
			obj.save()
			args["message"] = "Your opinion has been submited"
		else:
			args["message"] = "You posted nothing!"
	return JsonResponse(
            json.dumps(args),
            content_type="application/json",
            safe=False
        )