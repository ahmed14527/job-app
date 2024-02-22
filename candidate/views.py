from rest_framework import generics
from .models import MyApplyJobList, IsSortList
from .serializers import MyApplyJobListSerializer, IsSortListSerializer
from rest_framework import viewsets

class MyApplyJobListListCreateView(generics.ListCreateAPIView):
    queryset = MyApplyJobList.objects.all()
    serializer_class = MyApplyJobListSerializer

class MyApplyJobListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyApplyJobList.objects.all()
    serializer_class = MyApplyJobListSerializer

class IsSortListListCreateView(generics.ListCreateAPIView):
    queryset = IsSortList.objects.all()
    serializer_class = IsSortListSerializer

class IsSortListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IsSortList.objects.all()
    serializer_class = IsSortListSerializer
    
    

class MyApplyJobListViewSet(viewsets.ModelViewSet):
    queryset = MyApplyJobList.objects.all()
    serializer_class = MyApplyJobListSerializer

class IsSortListViewSet(viewsets.ModelViewSet):
    queryset = IsSortList.objects.all()
    serializer_class = IsSortListSerializer
