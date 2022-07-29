from django.urls import path
from .views import TeacherList

urlpatterns = [
    path('teacher/',TeacherList.as_view()),
    #path('teacher/<int:pk>/',TeacherDetail.as_view()),
]