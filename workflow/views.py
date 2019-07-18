from django.shortcuts import render
from django.http import HttpResponse

from .models import Action, ActionClass, Activity, ServiceType, Provider, ProviderServiceType, Task, TaskSequence, \
    ProviderTask, AdminTask, ProviderChoiceTask

from .forms import WorkflowForm


def index(request):

    # action_class_list = ActionClass.objects.all()
    # context = {'action_class_list': action_class_list}
    #return render(request, 'workflow/index.html', context)

    form = WorkflowForm()
    return render(request, 'workflow/index.html', {'form': form})


def action(request, action_id):
    action = Action.objects.get(id=action_id)
    context = {'action': action}
    return render(request, 'workflow/action.html', context)
    #return HttpResponse(f'Action {action_id} requested')


def activity(request):
    if request.method == 'GET':
        form = WorkflowForm(request.GET)
        if form.is_valid():
            activity = form.cleaned_data['activity']
            provider_service_type = form.cleaned_data['provider_service_type']

            """ based on the provider and service type choices, refine the task list """
            activity.set_provider_choice(provider_service_type)
            context = {'activity': activity,
                       'provider_service_type': provider_service_type}#, 'tasks': tasks}
            return render(request, 'workflow/activity.html', context)
    # activity = Activity.objects.get(id=activity_id)
    # context = {'activity': activity}
    # return render(request, 'workflow/activity.html', context)



def task(request, activity_id, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'workflow/task.html', context)
    #return HttpResponse(f'Task {task_id} in activity {activity_id} requested')