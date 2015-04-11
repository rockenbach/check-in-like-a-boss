# coding: utf-8
from django.db import models

class Workshop(models.Model):
	name = models.CharField(max_length=256)
	seats = models.IntegerField()

	def __unicode__(self):
		return u'%s' % self.name


class Participant(models.Model):
	name = models.CharField(max_length=256, blank=False, null=False)
	cpf = models.CharField(max_length=11, blank=False, help_text='Apenas números.')
	workshops = models.ManyToManyField(Workshop, related_name='participants')

	def __unicode__(self):
		return u'%s' % self.name