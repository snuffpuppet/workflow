from django import forms

from .models import Activity, Provider, ServiceType, ProviderServiceType


class WorkflowForm(forms.Form):
    provider_service_type = forms.ModelChoiceField(queryset=ProviderServiceType.objects.all(), empty_label=None)
    #service_type = forms.ModelChoiceField(queryset=ServiceType.objects.all(), empty_label=None)
    #provider = forms.ModelChoiceField(queryset=Provider.objects.all(), empty_label=None)
    activity = forms.ModelChoiceField(queryset=Activity.objects.all(), empty_label=None)

