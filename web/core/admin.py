from django.contrib import admin

from core import models


class ActionAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['task', 'state',]
        else:
            return []

    class Meta:
        model = models.Action

admin.site.register(models.Action, ActionAdmin)


class TaskAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        Given a Task instance save it to the database.
        """
        super().save_model(request, obj, form, change)
        models.Action.objects.create(task=obj)

    class Meta:
        model = models.Task

admin.site.register(models.Task, TaskAdmin)


admin.site.register(models.KandoUser)
admin.site.register(models.Tag)
