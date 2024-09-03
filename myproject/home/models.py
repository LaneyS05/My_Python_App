from django.db import models

class ProjectLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
