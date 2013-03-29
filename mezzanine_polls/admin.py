from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class PollAdmin(PageAdmin):
    inlines = (ChoiceInline, )

admin.site.register(Poll, PollAdmin)
