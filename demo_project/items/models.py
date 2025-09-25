from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.value})"

class ExternalPost(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=300)
    body = models.TextField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.external_id}: {self.title}"


