from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *


# HOME PAGE
@api_view(['GET'])
def home(request):
    """
    API endpoint for home page.
    """
    if request.method == 'GET':
        return Response({'Welcome to your home of Construction Management'}, status=status.HTTP_200_OK)


# PROJECT
@api_view(['GET', 'POST'])
def project_list(request):
    """
    API endpoint to list and create projects.
    """
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def project_details(request, pk):
    """
    API endpoint to get, update, and delete a project.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def project_daily_records(request, pk):
    """
    API endpoint to retrieve a specific project with all the dailyrecords associated with it.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'error': 'Project does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    daily_records = project.dailyrecord_set.all()  # Get all DailyRecords associated with the project
    
    serializer = DailyRecordSerializer(daily_records, many=True)  # Serialize the queryset
    
    return Response(serializer.data, status=status.HTTP_200_OK)

    # COMMENTS 
@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def comment_details(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# MATERIAL
@api_view(['GET', 'POST'])
def material_list(request):
    """
    API endpoint to list and create materials.
    """
    if request.method == "GET":
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def material_details(request, pk):
    """
    API endpoint to get, update, and delete a material.
    """
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = MaterialSerializer(material, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# MATERIAL USAGE
@api_view(['GET', 'POST'])
def material_usage_list(request):
    """
    API endpoint to list and create material usages.
    """
    if request.method == "GET":
        material_usages = MaterialUsage.objects.all()
        serializer = MaterialUsageSerializer(material_usages, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MaterialUsageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def material_usage_details(request, pk):
    """
    API endpoint to get, update, and delete a material usage.
    """
    try:
        material_usage = MaterialUsage.objects.get(pk=pk)
    except MaterialUsage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MaterialUsageSerializer(material_usage)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MaterialUsageSerializer(material_usage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = MaterialUsageSerializer(material_usage, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        material_usage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def dailyrecord_list(request):
    """
    API endpoint to list and create daily records.
    """
    if request.method == "GET":
        daily_records = DailyRecord.objects.all()
        serializer = DailyRecordSerializer(daily_records, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DailyRecordSerializer(data=request.data)
        if serializer.is_valid():
            daily_record = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def dailyrecord_details(request, pk):
    """
    API endpoint to get, update, and delete a daily record.
    """
    try:
        daily_record = DailyRecord.objects.get(pk=pk)
    except DailyRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DailyRecordSerializer(daily_record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DailyRecordSerializer(daily_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = DailyRecordSerializer(daily_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        daily_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def invoice_list(request):
    """
    API endpoint to list and create invoices.
    """
    if request.method == "GET":
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            invoice = serializer.save()
            
            # Bulk create InvoiceItem objects
            invoice_items_data = request.data.pop('invoice_items', [])
            invoice_items = [InvoiceItem(invoice=invoice, **item_data) for item_data in invoice_items_data]
            InvoiceItem.objects.bulk_create(invoice_items)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def invoice_details(request, pk):
    """
    API endpoint to get, update, and delete an invoice.
    """
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def create_blueprint(request):
    if request.method == 'GET':
        blueprints = Blueprint.objects.all()
        serializer = BlueprintSerializer(blueprints, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlueprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_record_pic(request):
    if request.method == 'GET':
        record_pics = RecordPics.objects.all()
        serializer = RecordPicsSerializer(record_pics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RecordPicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_building(request):
    if request.method == 'GET':
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
