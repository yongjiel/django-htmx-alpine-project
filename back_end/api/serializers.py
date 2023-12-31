from rest_framework import serializers
from .models import (Teacher, Subject, StudentProgress, Activity,
                     Resource, Coach, CoachTeacher, TeacherSubject,
                     ResourceTeacher)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)
    class Meta:
        model = Activity
        fields = [field.name for field in model._meta.fields]
        fields.append('teacher')
        read_only_fields = ['teacher']


class StudentProgressSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False, read_only=True)
    class Meta:
        model = StudentProgress
        fields = [field.name for field in model._meta.fields]
        fields.append('subject')
        read_only_fields = ['subject']


class ResourceSerializer(serializers.ModelSerializer):
    Teacher_set = TeacherSerializer(many=True, read_only=True)
    class Meta:
        model = Resource
        fields = [field.name for field in model._meta.fields]
        fields.append('Teacher_set')
        read_only_fields = ['Teacher_set']


class CoachSerializer(serializers.ModelSerializer):
    Teacher_set = TeacherSerializer(many=True, read_only=True)
    class Meta:
        model = Coach
        fields = [field.name for field in model._meta.fields]
        fields.append('Teacher_set')
        read_only_fields = ['Teacher_set']


class TeacherSubjectSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)
    subject = SubjectSerializer(many=False, read_only=True)
    class Meta:
        model = TeacherSubject
        fields = [field.name for field in model._meta.fields]
        fields.append('teacher')
        fields.append('subject')
        read_only_fields = ['teacher', 'subject']


class ResourceTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)
    resource = ResourceSerializer(many=False, read_only=True)
    class Meta:
        model = ResourceTeacher
        fields = [field.name for field in model._meta.fields]
        fields.append('teacher')
        fields.append('resource')
        read_only_fields = ['teacher', 'resource']


class CoachTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)
    coach = CoachSerializer(many=False, read_only=True)
    class Meta:
        model = CoachTeacher
        fields = [field.name for field in model._meta.fields]
        fields.append('teacher')
        fields.append('coach')
        read_only_fields = ['teacher', 'coach']