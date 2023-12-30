from django.shortcuts import render
from django.http import HttpResponse
import requests
from .config import Config
import json


def index(request):
    return render(request, 'index.html', locals())


def teachers(request):
    results = _get_data_from_remote('/api/teachers/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'teacher.html', context)


def activities(request):
    results = _get_data_from_remote('/api/activities/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'activity.html', context)


def subjects(request):
    results = _get_data_from_remote('/api/subjects/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'subject.html', context)


def student_progresses(request):
    results = _get_data_from_remote('/api/student_progresses/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'student_progress.html', context)


def resources(request):
    results = _get_data_from_remote('/api/resources/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'resource.html', context)


def coaches(request):
    results = _get_data_from_remote('/api/coaches/', request)
    context = {'results': results,
               'flash_flag': False}
    return render(request, 'coach.html', context)



def _get_data_from_remote(uri, request):
    # '/teachers/'
    url = Config.BACK_END_HOST + uri
    arg = ''
    if request.GET.get('q_teachers', ''):
        arg = "?q_teachers=" + request.GET.get('q_teachers', '')
    elif request.GET.get('q_teacher_activities', ''):
        arg = "?q_teacher_activities=" + request.GET.get('q_teacher_activities', '')
    elif request.GET.get('q_subjects', ''):
        arg = "?q_subjects=" + request.GET.get('q_subjects', '')
    elif request.GET.get('q_student_progresses', ''):
        arg = "?q_student_progresses=" + request.GET.get('q_student_progresses', '')
    elif request.GET.get('q_resources', ''):
        arg = "?q_resources=" + request.GET.get('q_resources', '')
    elif request.GET.get('q_coaches', ''):
        arg = "?q_coaches=" + request.GET.get('q_coaches', '')
    
    if arg:
        arg = arg.replace(' ', '%20')
        url = url  + arg

    data = requests.get(url)
    j = data.json()
    print("/////////")
    print(url)
    print(j)
    print(len(j))
    return j