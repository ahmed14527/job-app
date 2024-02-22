from rest_framework import serializers
from .models import MyApplyJobList, IsSortList

class MyApplyJobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApplyJobList
        fields = '__all__'

class IsSortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsSortList
        fields = '__all__'