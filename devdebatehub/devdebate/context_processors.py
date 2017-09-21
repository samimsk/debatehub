from UserApp.models import User
from django.template.context_processors import csrf 
from UserApp.forms import PersonRegistration


def add_variable_to_context(request):
	showlogin = True
	if request.user.is_authenticated():
		showlogin = False
	args = {}
	args['showlogin'] 	= showlogin
	args['test']		= 'sam'
	form		= PersonRegistration()
	args.update(csrf(request))
	return {
		'args'		: args,
		'form'		: form
	}