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
    if request.GET:
        arg += '?'
        tmp = []
        for k in request.GET:
            tmp.append( "{}=".format(k) + request.GET.get(k, '') )
        arg += "&".join(tmp)
    if arg:
        arg = arg.replace(' ', '%20')
        url = url  + arg

    data = requests.get(url)
    j = data.json()
    return j


def teacher_details(request):
    results = _get_data_from_remote('/api/teacher_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'teacher_details.html', context)


def teacher_activity_details(request):
    results = _get_data_from_remote('/api/teacher_activity_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'activity_details.html', context)


def subject_details(request):
    results = _get_data_from_remote('/api/subject_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'subject_details.html', context)


def student_progress_details(request):
    results = _get_data_from_remote('/api/student_progress_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'student_progress_details.html', context)


def  resource_details(request):
    results = _get_data_from_remote('/api/resource_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'resource_details.html', context)


def coach_details(request):
    results = _get_data_from_remote('/api/coach_details/', request)
    needed = request.GET.get('needed', '')
    context = {'results': results,
               'flash_flag': False,
               'needed': needed}
    return render(request, 'coach_details.html', context)
