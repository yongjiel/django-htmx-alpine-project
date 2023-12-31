from django.urls import path, include
from rest_framework import routers
from .views import (TeacherViewSet, SubjectViewSet,
                    StudentProgressViewSet, ResourceViewSet,
                    CoachViewSet, TeacherSubjectViewSet,
                    CoachTeacherViewSet, ResourceTeacherViewSet,
                    ActivityViewSet, TeacherDetailsViewSet, 
                    ActivityDetailsViewSet, SubjectDetailsViewSet,
                    StudentProgressDetailsViewSet, ResourceDetailsViewSet,
                    CoachDetailsViewSet, index)


router = routers.DefaultRouter()
router.register(r'teachers',
                TeacherViewSet,
                basename='teachers')  # for viewset
# router.register(r'teachers/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='teachers_id')
router.register(r'subjects',
                SubjectViewSet,
                basename='subject') 
# router.register(r'subjects/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='subjects_id')
router.register(r'student_progresses',
                StudentProgressViewSet,
                basename='student_progresses')
# router.register(r'student_progresses/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='student_progresses_id')
router.register(r'resources',
                ResourceViewSet,
                basename='resources')
# router.register(r'resources/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='resources_id')
router.register(r'coaches',
                CoachViewSet,
                basename='coaches')
# router.register(r'coaches/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='coaches_id')
router.register(r'activities',
                ActivityViewSet,
                basename='activities')
# router.register(r'activities/<int: pk>/',
#                 TeacherViewSet.as_view({'get': 'retrieve'}),
#                 basename='activities_id')
router.register(r'coach_teacher',
                CoachTeacherViewSet,
                basename='coach_teacher')
router.register(r'resource_teacher',
                ResourceTeacherViewSet,
                basename='resource_teacher')
router.register(r'teacher_subject',
                TeacherSubjectViewSet,
                basename='teacher_subject')
router.register(r'teacher_details',
                TeacherDetailsViewSet,
                basename='teacher_subject')
router.register(r'teacher_activity_details',
                ActivityDetailsViewSet,
                basename='teacher_subject')
router.register(r'subject_details',
                SubjectDetailsViewSet,
                basename='subject_details')
router.register(r'student_progress_details',
                StudentProgressDetailsViewSet,
                basename='student_progress_details')
router.register(r'resource_details',
                ResourceDetailsViewSet,
                basename='resource_details')
router.register(r'coach_details',
                CoachDetailsViewSet,
                basename='coach_details')

urlpatterns = [
    path('index', index),
    path('', include(router.urls))
]
