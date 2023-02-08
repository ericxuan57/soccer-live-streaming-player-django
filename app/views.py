from django.shortcuts import render
from .models import Soccer
from django.http import HttpResponse
from json import dumps
from datetime import datetime
def index(request):
    obj = Soccer.objects.all().values()

    data = []
    for row in obj:
        data.append(row)
    
    # dump data
    dataJSON = dumps(data, default=str)
    return render(request, 'index.html', {'data': dataJSON})

def get(request):
    strStartDateTime = request.GET["date"] + " " + request.GET["startTime"] + ":00"
    strEndDateTime = request.GET["date"] + " " + request.GET["endTime"] + ":00"
    startDateTime = datetime.strptime(strStartDateTime, '%Y-%m-%d %H:%M:%S')
    endDateTime = datetime.strptime(strEndDateTime, '%Y-%m-%d %H:%M:%S')

    
    filterData = Soccer.objects.filter(time_stamp__range=(startDateTime, endDateTime)).values()
    data = []
    for row in filterData:
        data.append(row)
    
    # dump data
    dataJSON = dumps(data, default=str)
    return HttpResponse(dataJSON)