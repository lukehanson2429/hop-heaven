from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    class Meta:
        verbose_name = 'email'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        blank=True)
    email = models.EmailField(max_length=40, null=False, blank=False)
    subject = models.CharField(max_length=60, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
