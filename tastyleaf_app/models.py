from django.db import models

class Story(models.Model):
	author = models.CharField(max_length=100, default='Anonymous', blank=True)
	fullstory = models.CharField(max_length=1000)
	quote = models.CharField(max_length=1000, default='Todo')
	question = models.CharField(max_length=200)
	home = models.CharField(max_length=100, default='Nothing', blank=True)
	approved = models.BooleanField(default=False)
	imgurl = models.CharField(max_length=300)

	def __unicode__(self):
		return self.author + self.quote + ' approved: ' + str(self.approved)
