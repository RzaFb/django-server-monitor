from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Server

@csrf_exempt
@require_POST
def add_server(request):
    try:
        address = request.POST['address']
        server = Server(address=address)
        server.save()
        response_data = {'id': server.id, 'message': 'Server added successfully'}
        return JsonResponse(response_data, status=201)
    except Exception as e:
        return HttpResponseBadRequest(f'Error: {str(e)}')

@require_GET
def get_server(request, id):
    server = get_object_or_404(Server, id=id)
    response_data = {
        'id': server.id,
        'address': server.address,
        'success': server.success,
        'failure': server.failure,
        'last_failure': server.last_failure.astimezone(timezone.get_current_timezone()).isoformat() if server.last_failure else None,
        'created_at': server.created_at.astimezone(timezone.get_current_timezone()).isoformat()
    }
    return JsonResponse(response_data)

@require_GET
def get_all_servers(request):
    servers = Server.objects.all()
    server_list = []
    for server in servers:
        server_data = {
            'id': server.id,
            'address': server.address,
            'success': server.success,
            'failure': server.failure,
            'last_failure': server.last_failure.timestamp() if server.last_failure else None,
            'created_at': server.created_at.timestamp()
        }
        server_list.append(server_data)
    return JsonResponse({'servers': server_list})