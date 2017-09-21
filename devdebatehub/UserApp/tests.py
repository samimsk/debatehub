from django.test import TestCase

# Create your tests here.
{{ profile.username }}
{{ profile.email }}
{{ profiledetails.name }}

class Debate(models.Model):
	hostedby 	= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'hosted_by')
	Title 		= models.CharField(max_length = 500, blank = False)
	Description = models.CharField(max_length = 1000, blank = False)

class ForAgainst(models.Model):
	topic 			= models.ForeignKey(Debate, on_delete = models.CASCADE, related_name = 'topic')
	name 			= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'name')
	supportunsupport= models.BooleanField(default = False)
