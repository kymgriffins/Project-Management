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
        serializer = ReadInvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = WriteInvoiceSerializer(data=request.data)
        if serializer.is_valid():
            invoice = serializer.save()
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def invoice_items(request):
    """
    API endpoint to list and create invoice items.
    """
    if request.method == "GET":
        invoice_items = InvoiceItem.objects.all()
        serializer = InvoiceItemSerializer(invoice_items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = InvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            invoice_item = serializer.save()
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
        serializer = ReadInvoiceSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WriteInvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = WriteInvoiceSerializer(invoice, data=request.data, partial=True)
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


@api_view(['GET', 'POST'])
def todo_list(request):
    """
    API endpoint to list and create Todo items.
    """
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def todo_detail(request, pk):
    """
    API endpoint to get, update, and delete a Todo item.
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def render_list(request):
    if request.method == 'GET':
        renders = Renders.objects.all()
        serializer = RenderSerializer(renders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def render_details(request, pk):
    try:
        render = Renders.objects.get(pk=pk)
    except Renders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RenderSerializer(render)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RenderSerializer(render, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = RenderSerializer(render, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        render.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def mep_list(request):
    if request.method == 'GET':
        mep_items = MEP.objects.all()
        serializer = MEPSerializer(mep_items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MEPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def mep_details(request, pk):
    try:
        mep_item = MEP.objects.get(pk=pk)
    except MEP.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MEPSerializer(mep_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MEPSerializer(mep_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = MEPSerializer(mep_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mep_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def structurals_list(request):
    if request.method == 'GET':
        structurals_items = Structurals.objects.all()
        serializer = StructuralsSerializer(structurals_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StructuralsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def structurals_details(request, pk):
    try:
        structurals_item = Structurals.objects.get(pk=pk)
    except Structurals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StructuralsSerializer(structurals_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StructuralsSerializer(structurals_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StructuralsSerializer(structurals_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        structurals_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import QS
from .serializers import QSSerializer

@api_view(['GET', 'POST'])
def qs_list(request):
    if request.method == 'GET':
        qs_items = QS.objects.all()
        serializer = QSSerializer(qs_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def qs_details(request, pk):
    try:
        qs_item = QS.objects.get(pk=pk)
    except QS.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QSSerializer(qs_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QSSerializer(qs_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = QSSerializer(qs_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qs_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Architecturals
from .serializers import ArchitecturalsSerializer

@api_view(['GET', 'POST'])
def architecturals_list(request):
    if request.method == 'GET':
        architecturals_items = Architecturals.objects.all()
        serializer = ArchitecturalsSerializer(architecturals_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArchitecturalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def architecturals_details(request, pk):
    try:
        architecturals_item = Architecturals.objects.get(pk=pk)
    except Architecturals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArchitecturalsSerializer(architecturals_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArchitecturalsSerializer(architecturals_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ArchitecturalsSerializer(architecturals_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        architecturals_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def legals_list(request):
    if request.method == 'GET':
        legals_items = Legals.objects.all()
        serializer = LegalsSerializer(legals_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LegalsSerializer(data=request.data)
        if serializer is valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def legals_details(request, pk):
    try:
        legals_item = Legals.objects.get(pk=pk)
    except Legals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LegalsSerializer(legals_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LegalsSerializer(legals_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = LegalsSerializer(legals_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        legals_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
