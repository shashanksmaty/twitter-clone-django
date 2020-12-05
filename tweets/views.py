from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet

def home_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Hello Django!</h1>")
  return render(request, 'pages/home.html', context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):  
  data = {
    "id": tweet_id
  }
  status = 200
  try:
    obj = Tweet.objects.get(id=tweet_id)
    data['content'] = obj.content
  except:
    data['message'] = "Tweet not found."
    status = 404
  return JsonResponse(data, status=status)