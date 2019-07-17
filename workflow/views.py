from django.shortcuts import render
from django.http import HttpResponse

from .models import Action, ActionClass, Activity, ServiceType, Provider, ProviderServiceType, Task, TaskSequence, \
    ProviderTask, AdminTask, ProviderChoiceTask


def index(request):
    action_class_list = ActionClass.objects.all()
    context = {'action_class_list': action_class_list}
    return render(request, 'workflow/index.html', context)


def action(request, action_id):
    action = Action.objects.get(id=action_id)
    context = {'action': action}
    return render(request, 'workflow/action.html', context)
    #return HttpResponse(f'Action {action_id} requested')


def activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    context = {'activity': activity}
    return render(request, 'workflow/activity.html', context)
    #return HttpResponse(f'Activity {activity_id} requested')


def task(request, activity_id, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'workflow/task.html', context)
    #return HttpResponse(f'Task {task_id} in activity {activity_id} requested')