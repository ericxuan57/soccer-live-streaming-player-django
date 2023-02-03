from django.core import serializers
from django.shortcuts import render
from django.views import View
from .models import Soccer
from json import dumps

class SoccerView(View):
    template = 'index.html'

    def get(self, request):
        obj = Soccer.objects.all().values()

        data = []
        for row in obj:
            data.append(row)
        
        # dump data
        dataJSON = dumps(data, default=str)
        return render(request, self.template, {'data': dataJSON})