from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'status', views.StatusViewSets, basename='status')

urlpatterns = [
    # path('status/', views.StatusGetPostApiView.as_view()),
    # path('all/<id>/', views.StatusUpdateRetrieveDeleteApiView.as_view()),
] + router.urls