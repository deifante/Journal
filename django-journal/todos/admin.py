from django.contrib import admin
from todos.models import TodoList
from todos.models import LineItem

class LineItemInline(admin.TabularInline):
    model = LineItem
    extra = 3
class TodoListAdmin(admin.ModelAdmin):
    inlines = [LineItemInline]
admin.site.register(TodoList, TodoListAdmin)
