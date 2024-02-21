from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import allowed_classes,geo_cordinates
import json
# Create your views here.

@csrf_exempt
def get_geo_location(request):
    data = json.loads(request.body.decode('utf-8'))    
    if 'branch' in data and 'student' in data and 'classNumber' in data and 'latitude' in data and 'longitude' in data:
        classes_qs = allowed_classes.objects.all().values('classes')
        classes_str = classes_qs[0]['classes']    
        if data['classNumber'] in classes_str.split(','):
            obj,created = geo_cordinates.objects.get_or_create(name=data['student'],branch=data['branch'],class_name=data['classNumber'])
            if created:
                obj.latitude=data['latitude']
                obj.longitude=data['longitude']
                obj.save()
                return JsonResponse({'data':True})
            else:
                return JsonResponse({'message':'Already Created'},status=401)
        else:
            return JsonResponse({'message':'Not allowed'},status=401)
    else:
        return JsonResponse({'message':'Parameters Missing'},status=401)