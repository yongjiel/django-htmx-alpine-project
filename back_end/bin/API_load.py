#!/usr/bin/env python 
# This program is to load the supplied .json file into Postgresql DB.
# flask server must be up.
# Usage: python API_load.py <json_file>
import os
import sys
import json
import requests 


PROTOCOL = os.environ.get('PROTOCOL', None) or 'http'
BACKENDPORT = os.environ.get('BACKENDPORT', None) or '8001'
BACKENDHOST =   os.environ.get('BACKENDSERVER', None) or '127.0.0.1'
BACK_END_HOST = f"{PROTOCOL}://{BACKENDHOST}:{BACKENDPORT}"  # if necessary, update it with your host
    

match = {"teacher_activities": f"{BACK_END_HOST}/teacher_activities",
         "student_progress": f"{BACK_END_HOST}/student_progresses",
         "resource_management": f"{BACK_END_HOST}/resource_management",
         'coach_details': f"{BACK_END_HOST}/coaches",
         'coach_teacher_interactions': f"{BACK_END_HOST}/coach_teacher_interactions"
         }


def post_and_get_id( name, url, key):
    temp = {'name': name}
    url2 = BACK_END_HOST + "/api/{}/".format(url)
    x = requests.post(url2, json=temp)
    if x.status_code not in [200, 201, 204]:
        print(url)
        print(key, temp)
        sys.exit(-1)
    return get_id(url, name, key, temp)


def get_id(url, name, key, temp):
    url3 = BACK_END_HOST + "/api/{}/?name={}".format(url, name)
    x = requests.get(url3)
    if x.status_code not in [200, 201, 204]:
        print(url3)
        print(key, temp)
        sys.exit(-1)
    else:
        j = x.json()
        return j[0]['id']


def load_to_db(key, value_list):
    if key=='teacher_activities':
        for v in value_list:
            for_teacher_activities(key, v)
    if key=='student_progress':
        for s in value_list:
            for_student_progress(key, s)
    if key=='resource_management':
        for r in value_list:
            for_resource_management(key, r)
    if key=='coach_details':
        for c in value_list:
            for_coach_details(key, c)
    if key=='coach_teacher_interactions':
        for ct in value_list:
            for_coach_teacher_interactions(key, ct)


def for_coach_teacher_interactions(key, value_list):
    # {
    #     "coach_id": 321,
    #     "teacher_id": 123,
    #     "last_meeting_date": "2023-11-08",
    #     "meeting_notes": "Discussed student engagement strategies."
    #   }
    url = BACK_END_HOST + "/api/coach_teacher/"
    value_list['coach'] = value_list['coach_id']
    value_list['teacher'] = value_list['teacher_id']
    del value_list['coach_id']
    del value_list['teacher_id']
    x = requests.post(url, value_list)
    if x.status_code not in [200, 201, 204]:
        print(key, value_list)
        sys.exit(-1)

def for_coach_details(key, value_list):
    # {
    #     "coach_id": 321,
    #     "name": "Emily Turner",
    #     "specialization": "Student Engagement",
    #     "years_of_experience": 5
    #   }
    value_list['id'] = value_list['coach_id']
    del value_list['coach_id']
    url = BACK_END_HOST + "/api/coaches/"
    x = requests.post(url, value_list)
    if x.status_code not in [200, 201, 204]:
        print(key, value_list)
        sys.exit(-1)


def for_resource_management(key, value_list):
    # {
    #     "resource_id": 2001,
    #     "resource_name": "Interactive Geometry Software",
    #     "allocated_teachers": [123],
    #     "utilization_rate": 87
    # }
    tmp = value_list['allocated_teachers']
    del value_list['allocated_teachers']
    value_list['id'] = value_list['resource_id']
    value_list['name'] = value_list['resource_name']
    del value_list['resource_id']
    del value_list['resource_name']
    url = BACK_END_HOST + "/api/resources/"
    x = requests.post(url, value_list)
    if x.status_code not in [200, 201, 204]:
        print(key, value_list)
        sys.exit(-1)
    for t in tmp:
        temp ={'teacher': t, 'resource': value_list['id']}
        url = BACK_END_HOST + "/api/resource_teacher/"
        x = requests.post(url, temp)
        if x.status_code not in [200, 201, 204]:
            print(key, temp)
            sys.exit(-1)


def for_student_progress(key, value_list):
    # {
    #     "class_id": 10,
    #     "subject": "Mathematics",
    #     "average_score_improvement": 12,
    #     "homework_completion_rate": 95,
    #     "attendance_rate": 98
    #   }
    o_id = post_and_get_id( value_list['subject'], 'subjects', key)
    del value_list['subject']
    value_list['subject'] = o_id
    url = BACK_END_HOST + "/api/student_progresses/"
    x = requests.post(url, value_list)
    if x.status_code not in [200, 201, 204]:
        print(key, value_list)
        sys.exit(-1)


def for_teacher_activities(key, value_list):
    # {
    #     "teacher_id": 123,
    #     "name": "John Doe",
    #     "last_active": "2023-11-10",
    #     "activity_score": 82,
    #     "student_interaction_rating": 4.5,
    #     "subjects_taught": ["Mathematics", "Physics"]
    #   }
    temp = {'id': value_list['teacher_id'],
            'name': value_list['name']}
    url = BACK_END_HOST + "/api/teachers/"
    x = requests.post(url, json=temp)
    if x.status_code not in [200, 201, 204]:
        print(x.status_code)
        print(url)
        print(key, temp)
        sys.exit(-1)

    for s in value_list['subjects_taught']:
        temp = {'name': s}
        url = BACK_END_HOST + "/api/subjects/"
        x = requests.post(url, json=temp)
        if x.status_code not in [200, 201, 204]:
            print(x.status_code)
            print(key, temp)
            sys.exit(-1)
    
    temp = value_list['subjects_taught']
    value_list['teacher'] = value_list['teacher_id']
    del value_list['teacher_id']
    del value_list['name']
    del value_list['subjects_taught']
    url = BACK_END_HOST + "/api/activities/"
    x = requests.post(url, json=value_list)
    if x.status_code not in [200, 201, 204]:
        print(key, value_list)
        sys.exit(-1)
    
    for s in temp:
        # get subject id first
        url = BACK_END_HOST + "/api/subjects/?name={}".format(s)
        x = requests.get(url)
        if x.status_code not in [200, 201, 204]:
            print(key, {'name': s})
            sys.exit(-1)
        else:
            j = x.json()
            subject = j[0]['id']
            # load to teacher_subject table
            url = BACK_END_HOST + "/api/teacher_subject/"
            x = requests.post(url, json={'teacher': value_list['teacher'],
                                         'subject': subject})
            if x.status_code not in [200, 201, 204]:
                print(key, value_list)
                sys.exit(-1)
    

def main():
    json_file = sys.argv[1]
    f = open(json_file, 'r')
    lst = f.readlines()
    content = json.loads(''.join(lst))
    for k in list(content.keys()):
        load_to_db(k, content[k])

if __name__== '__main__':
    
    main()

