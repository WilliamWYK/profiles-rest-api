from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('Hello-Viewset',views.HelloViewsets,base_name='Hello-Viewset')

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('',include(router.urls))
]



