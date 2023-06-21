from django.urls import path
from . import views


urlpatterns = [
 path('',views.CreateVListV.as_view()),
 path('<pk>',views.DeleteVUpdateV.as_view()),   
]
