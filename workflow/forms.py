from django import forms

from .models import Activity, Provider, ServiceType


class WorkflowForm(forms.Form):
    service_type = forms.ModelChoiceField(queryset=ServiceType.objects.all(), empty_label=None)
    provider = forms.ModelChoiceField(queryset=Provider.objects.all(), empty_label=None)
    activity = forms.ModelChoiceField(queryset=Activity.objects.all(), empty_label=None)

