"""
Models for Kando that will be responsible for the core business offering of the app.
"""
from django.db import models

from kandoauth.models import KandoUser
from tools.models import KandoModelBase


STATE_TO_DO = 0
STATE_DOING = 1
STATE_REVIEW = 2
STATE_DONE = 3
STATES = {
    STATE_TO_DO: 'to do',
    STATE_DOING: 'doing',
    STATE_REVIEW: 'review',
    STATE_DONE: 'done',
}


class Tag(KandoModelBase, models.Model):
    """
    Defines a class which helps label tasks according
    to the nature of the tasks for better management.
    """
    name = models.TextField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class TaskManager(models.Manager):
    """
    Custom manager to provide custom Task QuerySet
    """

    def create(self, **kwargs):
        """
        Create an Action with a to do state once
        a Task is created
        """
        obj = super().create(**kwargs)
        Action.objects.create(task=obj)
        return obj

    def to_do(self):
        """
        Return a QuerySet of all tasks in to do state
        """
        return self.tasks_with_state().filter(latest_action=STATE_TO_DO)

    def doing(self):
        """
        Return a QuerySet of all tasks in doing state
        """
        return self.tasks_with_state().filter(latest_action=STATE_DOING)

    def review(self):
        """
        Return a QuerySet of all tasks in review state
        """
        return self.tasks_with_state().filter(latest_action=STATE_REVIEW)

    def done(self):
        """
        Return a QuerySet of all tasks in done state
        """
        return self.tasks_with_state().filter(latest_action=STATE_DONE)

    def tasks_with_state(self):
        """
        A roundabout way to attach the latest Action's status to the Task QuerySet
        """
        return Task.objects.annotate(
            latest_action=models.F('action__state')
        ).order_by(
            'id',
            '-action__created'
        ).distinct()


class Task(KandoModelBase, models.Model):
    """
    The focal point of Kando. Represents a unit of work.
    """
    assignee = models.ForeignKey(
        KandoUser,
        related_name='tasks_to_do',
        help_text='Designates who assigned a task.')

    reviewer = models.ForeignKey(
        KandoUser,
        null=True,
        blank=True,
        related_name='tasks_to_review',
        help_text=(
            'Designates who will review a task. If no reviewer is set, assignee '
            'takes full responsibility for a task.'))

    name = models.TextField()
    description = models.TextField(blank=True, default='')
    due_date = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    objects = TaskManager()

    def __str__(self):
        return self.name


class Action(KandoModelBase, models.Model):
    """
    Keeps track of task history through its different states.
    """
    task = models.ForeignKey(
        Task,
        help_text='Designates task to be put in the action pipeline')

    state = models.IntegerField(choices=STATES.items(), default=STATE_TO_DO)

    def __str__(self):
        return '{} --> {}'.format(self.task, STATES[self.state])
