from django.db import models


class Base:
    def to_dict(self):
        return {column.name: getattr(self, column.name) 
                for column in self.__table__.columns}


class Teacher(models.Model, Base):
    # Basic model
    id = models.IntegerField(primary_key=True, null=False )
    name = models.CharField(max_length=100, null=False )
    class Meta:
        db_table = 'teacher'


class Activity(models.Model, Base):
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, 
                to_field='id', related_name='activities')
    # N to 1
    last_active = models.DateField( null=False, auto_now_add=True )
    activity_score = models.IntegerField(null=False)
    student_interaction_rating = models.FloatField(null=False)
    class Meta:
        db_table = 'activity'


class Subject(models.Model, Base):
    # Basic model
    name = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'subject'


class TeacherSubject(models.Model, Base):
    # N to N
    teacher = models.ForeignKey(Teacher, 
                    on_delete = models.CASCADE, 
                    to_field='id',
                    related_name='subjects')
    subject = models.ForeignKey(Subject,
                    on_delete = models.CASCADE, 
                    to_field='id',
                    related_name='teachers')
    class Meta:
        db_table = 'teacher_subject'
        unique_together = ('teacher_id', 'subject_id',)

    
class StudentProgress(models.Model, Base):
    # Basic model
    class_id = models.IntegerField(null=False, primary_key=True)
    subject = models.ForeignKey(Subject,
                                   on_delete = models.CASCADE, 
                                    to_field='id',
                                    related_name='student_progresses')
    average_score_improvement = models.IntegerField(null=False)
    homework_completion_rate = models.IntegerField(null=False)
    attendance_rate = models.IntegerField(null=False)
    class Meta:
        db_table = 'student_progress'
        unique_together = ('class_id', 'subject_id',)


class Resource(models.Model, Base):
    # Basic model
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    utilization_rate = models.IntegerField(null=False)
    class Meta:
        db_table = 'resource'


class ResourceTeacher(models.Model, Base):
    # N to N
    resource = models.ForeignKey(Resource,
                                    on_delete=models.CASCADE, 
                                    to_field='id',
                                    related_name='teachers')
    teacher = models.ForeignKey(Teacher,
                                    on_delete=models.CASCADE, 
                                    to_field='id',
                                    related_name='resources')
    class Meta:
        db_table = 'resource_teacher'
        unique_together = ('resource_id', 'teacher_id',)
    

class Coach(models.Model, Base):
    # Basic model
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    specialization = models.CharField(max_length=100, null=False)
    years_of_experience = models.IntegerField(null=False)
    class Meta:
        db_table = 'coach'


class CoachTeacher(models.Model, Base):
    # N to N
    coach = models.ForeignKey(Coach, 
                                    on_delete=models.CASCADE,
                                    to_field='id',
                                    related_name='teachers')
    teacher = models.ForeignKey(Teacher,
                                   on_delete=models.CASCADE,
                                    to_field='id',
                                    related_name='coaches')
    last_meeting_date = models.DateField(auto_now_add=True, null=False)
    meeting_notes = models.CharField(max_length=512, null=False)
    class Meta:
        db_table = 'coach_teacher'
        unique_together=('coach_id', 'teacher_id',)

