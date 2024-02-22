from rest_framework import serializers
from .models import Hr, JobPost, CandidateApplications, SelectCandidateJob

class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

class CandidateApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateApplications
        fields = '__all__'

class SelectCandidateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectCandidateJob
        fields = '__all__'