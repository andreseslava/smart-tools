from django import forms

from contests.models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('name', 'prize', 'startDate', 'endDate', 'path', 'logo')
