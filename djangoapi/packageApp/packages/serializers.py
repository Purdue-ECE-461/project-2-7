from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer):

    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        test = bytes(obj.content)
        return test


    class Meta:
        model = Package
        fields = ('id', 'name', 'content')