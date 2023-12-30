from django.urls import path
from .views import (index, teachers, activities, subjects,
                    student_progresses, resources, coaches)

urlpatterns = [
    path('', index, name='index'),
    path('teachers/', teachers, name='teachers'),
    path('teacher_activities/', activities, name='activities'),
    path('subjects/', subjects, name='subjects'),
    path('student_progresses/', student_progresses, name='student_progresses'),
    path('resource_management/', resources, name='resources'),
    path('coaches/', coaches, name='coaches'),
]
