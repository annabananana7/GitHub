from django.contrib import admin
from todo.models import Todo, Item

class TodoInline(admin.TabularInline):
    model = Item
    extra = 3

class TodoAdmin(admin.ModelAdmin):
    fields = ['name', 'created']
    inlines = [TodoInline]
    list_display = ('name', 'created')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Item)
