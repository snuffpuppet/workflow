from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class ActionClass(models.Model):
    """ Provide, Change, Cancel """
    def __str__(self):
        return self.name

    def related_activities(self):
        #return Action.objects.filter(action_class=self)
        #return Activity.objects.all()
        return Activity.objects.filter(action__action_class=self)
        #actions = self.action_set.filter(activity__id__gte=0)
        #return actions[0].activity_set.all()
        # return [activity
        #         for action in self.action_set.all()
        #         for activity in action.activity_set.all()]

    name = models.CharField(max_length=50)


class Action(models.Model):
    """ Actual Actions on a service such as transition, upgrade, new, cancel """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    action_class = models.ForeignKey(ActionClass, on_delete=models.CASCADE)


class ServiceType(models.Model):
    """ Service we are acting upon such as NBN Carriage or Standalone router"""
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)


class Provider(models.Model):
    """ Service provider such as Optus or iiNet or even OTW """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)


class ProviderServiceType(models.Model):
    """ Link Service Providers to the types of service they provide """
    def __str__(self):
        return self.provider.name + " " + self.service_type.name

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)


class Activity(models.Model):
    """ A complete provisioning activity with a sequence of tasks"""
    def __str__(self):
        return self.action.__str__()

    def name(self):
        return self.action.name

    def task_sequence(self):
        return self.tasksequence_set.all().order_by('sequence').select_related('task')

    def tasks(self):
        return Task.objects.filter(tasksequence__activity=self).order_by('tasksequence__sequence')
        #return self.tasksequence_set.all().order_by('sequence')

    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    summary = models.CharField(max_length=200)


class Task(models.Model):
    def __str__(self):
        return self.name()

    def is_admin_task(self):
        return hasattr(self, 'admintask')

    def is_provider_task(self):
        return hasattr(self, 'providertask')

    def is_provider_choice_task(self):
        return hasattr(self, 'providerchoicetask')

    def is_choice_task(self):
        return self.is_provider_choice_task()

    def has_instructions(self):
        return self.is_admin_task() or self.is_provider_task()

    def instructions(self):
        if self.is_admin_task():
            return self.admintask.instructions
        elif self.is_provider_task():
            return self.providertask.instructions
        else:
            raise ObjectDoesNotExist(f'Task {self.name} does not have instructions')

    def choices(self):
        if self.is_provider_choice_task():
            action = self.providerchoicetask.action
            return ProviderTask.objects.all().filter(action=action)
        else:
            ObjectDoesNotExist(f'Task {self.name} does not have task choices')

    def name(self):
        if self.is_admin_task():
            return self.admintask.__str__()
        elif self.is_provider_task():
            return self.providertask.__str__()
        elif self.is_provider_choice_task():
            return self.providerchoicetask.__str__()
        else:
            return f'{self.pk}'

    #class Meta:
    #    abstract = True


class AdminTask(models.Model):
    def __str__(self):
        return f'{self.name}'

    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    instructions = models.TextField()


class ProviderTask(models.Model):
    def __str__(self):
        return self.name()

    def name(self):
        return f'{self.action.name} {self.provider_service_type.__str__()}'

    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    provider_service_type = models.ForeignKey(ProviderServiceType, on_delete=models.CASCADE)
    instructions = models.TextField()


class ProviderChoiceTask(models.Model):
    def __str__(self):
        return f'Engage Service Provider ({self.action.name})'

    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    #heading = models.CharField(max_length=50)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)


class TaskSequence(models.Model):
    def __str__(self):
        return f"[{self.sequence}] -> {self.task.__str__()}"

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    sequence = models.IntegerField(default=1)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""
