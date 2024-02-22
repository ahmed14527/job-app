from rest_framework import generics
from .models import Hr, JobPost, CandidateApplications, SelectCandidateJob
from .serializers import HrSerializer, JobPostSerializer, CandidateApplicationsSerializer, SelectCandidateJobSerializer

class HrListCreateView(generics.ListCreateAPIView):
    queryset = Hr.objects.all()
    serializer_class = HrSerializer

class HrRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hr.objects.all()
    serializer_class = HrSerializer

class JobPostListCreateView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class CandidateApplicationsListCreateView(generics.ListCreateAPIView):
    queryset = CandidateApplications.objects.all()
    serializer_class = CandidateApplicationsSerializer

class CandidateApplicationsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateApplications.objects.all()
    serializer_class = CandidateApplicationsSerializer

class SelectCandidateJobListCreateView(generics.ListCreateAPIView):
    queryset = SelectCandidateJob.objects.all()
    serializer_class = SelectCandidateJobSerializer

class SelectCandidateJobRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SelectCandidateJob.objects.all()
    serializer_class = SelectCandidateJobSerializer
    
    
    
from rest_framework import viewsets

class HrViewSet(viewsets.ModelViewSet):
    queryset = Hr.objects.all()
    serializer_class = HrSerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class CandidateApplicationsViewSet(viewsets.ModelViewSet):
    queryset = CandidateApplications.objects.all()
    serializer_class = CandidateApplicationsSerializer

class SelectCandidateJobViewSet(viewsets.ModelViewSet):
    queryset = SelectCandidateJob.objects.all()
    serializer_class = SelectCandidateJobSerializer