from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Chat(models.Model):
    content = models.TextField()
    user = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user