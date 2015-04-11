# coding: utf-8
from django.contrib import admin
from django.contrib import messages
from django.forms import ValidationError
from checkin.models import Workshop, Participant
from checkin.forms import WorkshopForm, ParticipantForm

class WorkshopAdmin(admin.ModelAdmin):
	form = WorkshopForm


class ParticipantAdmin(admin.ModelAdmin):
	form = ParticipantForm

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)