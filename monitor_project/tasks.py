from celery import shared_task
import requests
from server.models import Server
from django.utils import timezone

@shared_task
def health_check():
    servers = Server.objects.all()

    for server in servers:
        try:
            response = requests.get(server.address, timeout=5)
            if response.status_code == 200:
                server.success += 1
            else:
                server.failure += 1
                server.last_failure = timezone.now()
            server.save()
        except requests.RequestException:
            server.failure += 1
            server.last_failure = timezone.now()
            server.save()