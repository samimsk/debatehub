from django.db import models
from devdebatehub.settings import AUTH_USER_MODEL



class Debate(models.Model):
	hostedby 	= models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'hosted_by')
	title 		= models.CharField(max_length = 500, blank = False)
	description = models.CharField(max_length = 1000, blank = False)
	stat		= models.IntegerField(default = 0)
	opinioncount= models.IntegerField(default = 0)

	def __str__(self):
		return self.hostedby.username + "--" + self.title
	class Meta:
		ordering = ["-opinioncount"]


class ForAgainst(models.Model):
	topic 			= models.ForeignKey(Debate, on_delete = models.CASCADE, related_name = 'topic_foragainst')
	name 			= models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'name')
	supportunsupport= models.BooleanField(default = False)

	def __str__(self):
		return self.name.username + " " + str(self.topic.pk)



class Opinion(models.Model):
	topic 	= models.ForeignKey(Debate, on_delete = models.CASCADE, related_name = 'topic_opinion')
	title   = models.CharField(max_length = 100, blank = True, null = True)
	description = models.CharField(max_length = 2000, blank = False )
	opinionby = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'opinion_by')
	fororagainst = models.BooleanField(default = True)
	legit = models.IntegerField(default = 0)

	def __str__(self):
		return self.opinionby.username + 'posted an opinion'

	class Meta:
		ordering = ["-legit", "-id"]


class OpinionRating(models.Model):
	opinion 	= models.ForeignKey(Opinion, on_delete = models.CASCADE, related_name = 'opinion_rating')
	rated_by	= models.ManyToManyField(AUTH_USER_MODEL)
	rating 		= models.IntegerField(default = 0, blank = False)

	def __str__(self):
		return self.opinion.topic.title + "-rating-" + str(self.rating)


class Blog(models.Model):
	writtenby 	= models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'blog_written_by')
	heading 	= models.CharField(max_length = 100, blank = False)
	description = models.CharField(max_length = 2000, blank = False )

	def __str__(self):
		return self.writtenby.username + ' have written a blog post'

