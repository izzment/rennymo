from django.contrib import admin
from .models import Message, Tag, Event

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'tag')


admin.site.register(Message, ContactAdmin)
admin.site.register(Tag)
admin.site.register(Event)