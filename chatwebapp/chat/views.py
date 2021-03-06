from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
def index(request):
  return render(request, 'chat/index.html')

def room(request, room_name):
  return render(request, 'chat/room.html', {
    'room_name': room_name
  })

def alarm(req):
  layer = get_channel_layer()
  async_to_sync(layer.group_send)('chat_lobby', {
    'type': 'send_from_view',
    'content': 'triggered'
  })

  return HttpResponse('<p>Done<p>')
