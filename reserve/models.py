from django.db import models

# Create your models here.

class post(models.Model):
	POST_TYPE_OPTIONS = (
		#(value,show name)
		('tu', 'Tutorial'),
		('fx', 'Fix'),
	)
	post_type = models.CharField(
		max_length=2,
		choices=POST_TYPE_OPTIONS,
		default='tu',
	)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
    
	class Meta:
		ordering = ['post_type', 'title']

	def __str__(self):
		return '{0} - {1}'.format(self.post_type, self.title)

class tutorial(models.Model):
	forpost = models.ForeignKey(
		'Post', 
		on_delete = models.CASCADE, 
		null=True, 
		blank=True,
		)
	steps = models.IntegerField(blank=True, default = 0)
	pic = models.CharField(blank=True, max_length=100)
	content = models.TextField(blank=True)
	
	class Meta:
		ordering = ['forpost', 'steps']
	
	def __str__(self):
		return '{0} - No. {1}'.format(self.forpost.title, str(self.steps))
