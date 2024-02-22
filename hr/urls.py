from django.urls import path,include
from rest_framework import routers
from .views import HrViewSet, JobPostViewSet, CandidateApplicationsViewSet, SelectCandidateJobViewSet
from .views import (
    HrListCreateView,
    HrRetrieveUpdateDestroyView,
    JobPostListCreateView,
    JobPostRetrieveUpdateDestroyView,
    CandidateApplicationsListCreateView,
    CandidateApplicationsRetrieveUpdateDestroyView,
    SelectCandidateJobListCreateView,
    SelectCandidateJobRetrieveUpdateDestroyView
)
router = routers.DefaultRouter()
router.register(r'hr', HrViewSet)
router.register(r'jobpost', JobPostViewSet)
router.register(r'candidateapplications', CandidateApplicationsViewSet)
router.register(r'selectcandidatejob', SelectCandidateJobViewSet)


urlpatterns = [
    # Hr URLs
    path('hr/', HrListCreateView.as_view(), name='hr-list-create'),
    path('hr/<int:pk>/', HrRetrieveUpdateDestroyView.as_view(), name='hr-retrieve-update-destroy'),

    # JobPost URLs
    path('jobpost/', JobPostListCreateView.as_view(), name='jobpost-list-create'),
    path('jobpost/<int:pk>/', JobPostRetrieveUpdateDestroyView.as_view(), name='jobpost-retrieve-update-destroy'),

    # CandidateApplications URLs
    path('candidateapplications/', CandidateApplicationsListCreateView.as_view(), name='candidateapplications-list-create'),
    path('candidateapplications/<int:pk>/', CandidateApplicationsRetrieveUpdateDestroyView.as_view(), name='candidateapplications-retrieve-update-destroy'),

    # SelectCandidateJob URLs
    path('selectcandidatejob/', SelectCandidateJobListCreateView.as_view(), name='selectcandidatejob-list-create'),
    path('selectcandidatejob/<int:pk>/', SelectCandidateJobRetrieveUpdateDestroyView.as_view(), name='selectcandidatejob-retrieve-update-destroy'),
    path('', include(router.urls)),

]