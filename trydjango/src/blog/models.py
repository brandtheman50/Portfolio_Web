from django.db import models

class Blog(models.Model):
    NONE = 'None'
    Post_Subject = models.CharField(max_length=50,blank=False) #maximum length
    Summary = models.TextField(blank=False, null=False)
