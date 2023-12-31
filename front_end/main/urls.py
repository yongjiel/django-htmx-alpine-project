from django.urls import path
from .views import (index, teachers, activities, subjects,
                    student_progresses, resources, coaches,
                    teacher_details, teacher_activity_details,
                    student_progress_details, resource_details,
                    coach_details, subject_details)

urlpatterns = [
    path('', index, name='index'),
    path('teachers/', teachers, name='teachers'),
    path('teacher_activities/', activities, name='activities'),
    path('subjects/', subjects, name='subjects'),
    path('student_progresses/', student_progresses, name='student_progresses'),
    path('resource_management/', resources, name='resources'),
    path('coaches/', coaches, name='coaches'),
    path('teacher_details/', teacher_details, name='teacher_details'),
    path('teacher_activity_details/', teacher_activity_details, name='teacher_activity_details'),
    path('student_progress_details/', student_progress_details, name='student_progress_details'),
    path('resource_details/', resource_details, name='resource_details'),
    path('coach_details/', coach_details, name='coach_details'),
    path('subject_details/', subject_details, name='subject_details'),
    
]
