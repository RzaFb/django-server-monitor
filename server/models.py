from django.db import models
from django.utils import timezone

class Server(models.Model):
    address = models.CharField(max_length=255)
    success = models.IntegerField(default=0)
    failure = models.IntegerField(default=0)
    last_failure = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"Server {self.id}: {self.address}"