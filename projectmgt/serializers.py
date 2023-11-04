from rest_framework import serializers
from authentication.models import User
from authentication.serializer import UserSerializer
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    architect = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    foreman = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    supervisor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # architect = UserSerializer()
    # foreman = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'
        depth = 1



class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'name', 'description', 'unit_cost')
        depth = 1


class MaterialUsageSerializer(serializers.ModelSerializer):
    material= serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())
    daily_record =serializers.PrimaryKeyRelatedField(queryset=DailyRecord.objects.all())

    class Meta:
        model = MaterialUsage
        fields = '__all__'
        depth = 1


class DailyRecordSerializer(serializers.ModelSerializer):
    # add materials serializer
    # materials = MaterialUsageSerializer(many=True)
    project= serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
   

    class Meta:
        model = DailyRecord
        fields = '__all__'
        depth = 1




class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class InvoiceItemSerializer(serializers.ModelSerializer):
    # materials= serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())
    # invoice= serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        depth = 1
class ReadInvoiceSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    invoices = InvoiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 2
class WriteInvoiceSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    invoices = serializers.PrimaryKeyRelatedField(many=True, queryset=InvoiceItem.objects.all(), allow_empty=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    
class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = '__all__'

class RecordPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordPics
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
        



class TodoSerializer(serializers.ModelSerializer):
    # todo = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Todo
        fields = '__all__'
        depth = 1