from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core import serializers
from adult.models import *
import json
# Create your views here.

def index(request):
	return render(request, 'adult/index.html')

def popStats(request):
	responseData={}
	responseData['male']=adult.objects.filter(sex=2).count()
	responseData['female']=adult.objects.filter(sex=1).count()
	responseData['Wife']=adult.objects.filter(relationship=1).count()
	responseData['OwnChild']=adult.objects.filter(relationship=2).count()
	responseData['Husband']=adult.objects.filter(relationship=3).count()
	responseData['Notinfamily']=adult.objects.filter(relationship=4).count()
	responseData['OtherRelatives']=adult.objects.filter(relationship=4).count()
	responseData['Unmarried']=adult.objects.filter(relationship=5).count()
	print(responseData)
	#responseData=serializers.serialize('json',responseData)
	#return JsonResponse(responseData)
	# loaded = json.loads(json_data)
	return render(request,'adult/displayChart.html',{'responseData':responseData})
	#return HttpResponse(responseData, context_type="application/json")


# responseData={}
# responseData['male']=adult.objects.filter(sex=2).count()
# responseData['female']=adult.objects.filter(sex=1).count()
# responseData['Wife']=adult.objects.filter(relationship=1).count()
# responseData['OwnChild']=adult.objects.filter(relationship=2).count()
# responseData['Husband']=adult.objects.filter(relationship=3).count()
# responseData['Notinfamily']=adult.objects.filter(relationship=4).count()
# responseData['OtherRelatives']=adult.objects.filter(relationship=4).count()
# responseData['Unmarried']=adult.objects.filter(relationship=5).count()