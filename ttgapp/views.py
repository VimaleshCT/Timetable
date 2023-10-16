from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONparser
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse

# Create your views here.
from ttgapp.models import Admin
from ttgapp.serializers import AdminSerializer

@csrf_exempt
def AdminApi(request,id=0):
    if request.method == 'GET':
        admin = Admin.objects.all()
        Admin_serializer=AdminSerializer(admin,many=True)
        return JsonResponse(Admin_serializer.data,safe=False)
    elif request.method =='POST':
        Admin_data =JSONParser().parse(request)
        Admin_serializer=AdminSerializer(data=Admin_data)
        if Admin_serializer.is_valid():
            Admin_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Admin_data=JSONParser().parse(request)
        admin=Admin.objects.get(Facultyid =Admin_data['Facultyid'])
        Admin_serializer=AdminSerializer(admin,data=Admin_data)
        if Admin_serializer.is_valid():
            Admin_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        admin=Admin.objects.get(Facultyid= id)
        admin.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    