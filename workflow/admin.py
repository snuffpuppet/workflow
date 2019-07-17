from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from pagedown.widgets import AdminPagedownWidget

from .models import Action, ActionClass, Activity, ServiceType, Provider, ProviderServiceType, Task, TaskSequence, \
    ProviderTask, AdminTask, ProviderChoiceTask

# from workflow.models import Action, ActionClass, Activity, ServiceType, Provider, ProviderServiceType, Task, TaskSequence, ProviderTask, AdminTask, ProviderChoiceTask


class TaskSequenceInline(admin.StackedInline):
    model = TaskSequence
    extra = 3


class ProviderTaskInline(admin.TabularInline):
    model = ProviderTask


class AdminTaskInline(admin.TabularInline):
    model = AdminTask


class ProviderChoiceTaskInline(admin.TabularInline):
    model = ProviderChoiceTask


class TaskListFilter(admin.SimpleListFilter):
    title = _('task type')
    parameter_name = 'task type'

    def lookups(self, request, model_admin):
        static_choices = (
            ('admin', _('administration tasks')),
            ('provider', _('service provider tasks')),
            ('provider choice', _('service provider choices')),
        )
        service_type_choices = tuple((f'st:{st.name}', _(f'{st.name}'))
                                     for st in ServiceType.objects.all())

        provider_choices = tuple((f'pv:{pv.name}', _(f'{pv.name}'))
                                 for pv in Provider.objects.all())

        return static_choices + service_type_choices + provider_choices


    def queryset(self, request, queryset):
        if self.value() == 'admin':
            return queryset.filter(admintask__pk__isnull=False)
        if self.value() == 'provider':
            return queryset.filter(providertask__pk__isnull=False)
        if self.value() == 'provider choice':
            return queryset.filter(providerchoicetask__pk__isnull=False)

        """ process provider and service type based filters """
        filter_type = self.value()[:2]
        filter_by = self.value()[3:]

        if filter_type == 'st':
            return queryset.filter(providertask__provider_service_type__service_type__name=filter_by)

        if filter_type == 'pv':
            return queryset.filter(providertask__provider_service_type__provider__name=filter_by)

class TaskAdmin(admin.ModelAdmin):
    inlines = [ProviderTaskInline, AdminTaskInline, ProviderChoiceTaskInline]
    list_filter = (TaskListFilter,)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['action', 'summary']}),
    ]
    inlines = [TaskSequenceInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(Activity, ActivityAdmin)

admin.site.register(ServiceType)
admin.site.register(Provider)
admin.site.register(ProviderServiceType)
admin.site.register(ActionClass)
admin.site.register(Action)

