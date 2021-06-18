from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('Hello-Viewset',views.HelloViewsets,base_name='Hello-Viewset')
router.register('profiles',views.UserProfilesViewSets)
router.register('feed',views.UserProfileFeedViewSets)

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]



