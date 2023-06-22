from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('student',views.StudentViewset,basename='student')

urlpatterns = [
    path('api/',include(router.urls))
]
