from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.name

class Item(models.Model):
    todo = models.ForeignKey(Todo)
    todo_text = models.CharField(max_length=150)

    def __unicode(self):
        return self.todo_text
