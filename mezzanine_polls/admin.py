from django.contrib import admin
from django.utils.translation import ugettext as _
from mezzanine.pages.admin import PageAdmin
from .models import Poll, Choice
from copy import deepcopy


class ChoiceInline(admin.TabularInline):
    model = Choice

class PollAdmin(PageAdmin):
    inlines = (ChoiceInline, )

admin.site.register(Poll, PollAdmin)
