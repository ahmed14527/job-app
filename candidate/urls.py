from django.urls import path
from django.urls import include, path
from rest_framework import routers
from .views import MyApplyJobListViewSet, IsSortListViewSet
from .views import (
    MyApplyJobListListCreateView,
    MyApplyJobListRetrieveUpdateDestroyView,
    IsSortListListCreateView,
    IsSortListRetrieveUpdateDestroyView
)


router = routers.DefaultRouter()
router.register(r'myapplyjoblist', MyApplyJobListViewSet)
router.register(r'issortlist', IsSortListViewSet)


urlpatterns = [
    path('myapplyjoblist/', MyApplyJobListListCreateView.as_view(), name='myapplyjoblist-list-create'),
    path('myapplyjoblist/<int:pk>/', MyApplyJobListRetrieveUpdateDestroyView.as_view(), name='myapplyjoblist-retrieve-update-destroy'),
    path('issortlist/', IsSortListListCreateView.as_view(), name='issortlist-list-create'),
    path('issortlist/<int:pk>/', IsSortListRetrieveUpdateDestroyView.as_view(), name='issortlist-retrieve-update-destroy'),
    path('', include(router.urls)),

]