from django.db.models import fields
from rest_framework import serializers
from .models import Package, data, metadata


class DataSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        test = bytes(obj.content)
        return test
    
    class Meta:
        model = data
        fields = ('content', 'url', 'JSProgram')
        
class MetaDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = metadata
        fields = ('Name', 'Version')

class PackageSerializer(serializers.ModelSerializer):

    metadata = MetaDataSerializer(required=True)
    data = DataSerializer(required=True)

    class Meta:
        model = Package
        fields = ('metadata', 'data')
        
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        data_data = validated_data.pop('data')
        data = DataSerializer.create(DataSerializer(), validated_data=data_data)
        metadata_data = validated_data.pop('metadata')
        metadata = MetaDataSerializer.create(MetaDataSerializer, validated_data=metadata_data)
        package, created = Package.objects.update_or_create(data=data, metadata=metadata)
        return package