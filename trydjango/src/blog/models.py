from django.db import models

class Blog(models.Model):
    post_subject = models.TextField()
    summary = models.TextField()
