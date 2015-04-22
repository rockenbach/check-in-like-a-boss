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
	list_filter = ('workshops__name',)
	search_fields = ('name', )
	actions = None


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)