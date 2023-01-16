from rest_framework.serializers import ModelSerializer
from .models import User 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','roles']
        
        
        def create(self,validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            instance.is_active = True
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance