from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^stories/$', views.feedstories, name = 'stories'),
	url(r'^user/', include('UserApp.urls')),
	url(r'^title/(?P<debate_id>\w+)/$', views.debatedetail, name = 'debatedetail'),
	url(r'^votefor/(?P<debate_id>\w+)/$', views.votefor, name = 'votefor'),
	url(r'^unvotefor/(?P<debate_id>\w+)/$', views.unvotefor, name = 'unvotefor'),
	url(r'^submitopinion/(?P<debate_id>\w+)/$', views.submitopinion, name = 'submitopinion'),
	url(r'^legit/(?P<debate_id>\w+)/(?P<opinion_id>\w+)/$', views.legit, name = 'legit')

]