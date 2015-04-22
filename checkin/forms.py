# coding: utf-8
from django import forms
from checkin.models import Workshop, Participant


class WorkshopForm(forms.ModelForm):

	class Meta:
		model = Workshop
		fields = '__all__'

	def clean(self):
		cleaned_data = super(WorkshopForm, self).clean()

		if self.instance.pk:
			current_seats_number = self.instance.participants.count()
			new_seats_number = cleaned_data.get('seats')
			if current_seats_number > new_seats_number:
				raise forms.ValidationError(
					u'O workshop "%s" já possui "%s" inscritos. Por favor, informe uma quantidade de assentos maior que "%s".' % (cleaned_data.get('name'), current_seats_number, new_seats_number)
				)
		return cleaned_data


class ParticipantForm(forms.ModelForm):

	workshops = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple(),
		queryset=Workshop.objects.all()
	)


	class Meta:
		model = Participant
		fields = '__all__'

	def clean(self):
		cleaned_data = super(ParticipantForm, self).clean()
		selected_workshops = cleaned_data.get('workshops', ())

		for workshop in selected_workshops:
			if workshop.participants.count() >= workshop.seats:
				raise forms.ValidationError(
					u'O workshop "%s" já está lotado.' % workshop.name
				)

		return cleaned_data