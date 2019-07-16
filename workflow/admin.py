from django.contrib import admin
from django.db import models

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


class TaskAdmin(admin.ModelAdmin):
    inlines = [ProviderTaskInline, AdminTaskInline, ProviderChoiceTaskInline]
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

