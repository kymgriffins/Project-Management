from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = '__all__'
        depth = 1

class TaskSerializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = '__all__'
        depth = 1

class TeamSerializer(serializers.ModelSerializer):
    class Meta :
        model = Team
        fields = '__all__'
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'
        depth = 1