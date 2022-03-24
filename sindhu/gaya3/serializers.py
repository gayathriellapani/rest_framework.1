from rest_framework.serializers import ModelSerializer
from.models import Student
class Studentserializer(ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"