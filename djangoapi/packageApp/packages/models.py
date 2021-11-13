from django.db import models
from django.db.models.fields import BinaryField

# Create your models here.

class data(models.Model):
    content = models.BinaryField()
    url = models.CharField()
    JSProgram = models.TextField()

    def __str__(self) -> str:
        return self.url

class metadata(models.Model):
    Name = models.CharField(max_length=70)
    Version = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.Name

class Package(models.Model):
    metadata = models.OneToOneField(metadata, on_delete=models.CASCADE)
    data = models.OneToOneField(data, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.metadata.Name

