from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from mezzanine.pages.models import Page


class Poll(Page):

    def __unicode__(self):
        return u'%s' % (self.title, )

    class Meta:
        verbose_name = _('Poll')


class Choice(models.Model):
    poll = models.ForeignKey('Poll')
    text = models.CharField(max_length=256)

    def __unicode__(self):
        return u'\'%s\' in Poll \'%s\'' % (
            self.text,
            self.poll.title
        )


class Vote(models.Model):
    choice = models.ForeignKey('Choice')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Vote by %s for Choice \'%s\' in Poll \'%s\'' % (
            self.user,
            self.choice.text,
            self.choice.poll.title
        )
