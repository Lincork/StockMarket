import json
from datetime import datetime, timedelta
from SMDjango.GetData import get_share_price
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def stock_data(request):
    now = datetime.now()
    start = request.GET.get('start', now.replace(hour=9,second=0,microsecond=0))
    ended = request.GET.get('ended', now)
    instrument = request.GET.get('instrument', '')
    share_price = get_share_price(instrument, start, ended)
    return JsonResponse(share_price, safe=False)

