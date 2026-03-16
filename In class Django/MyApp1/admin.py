from django.contrib import admin
from .models import teacher
from .models import assessment
from .models import Course
from .models import Student
# Register your models here.
admin.site.register(teacher)
admin.site.register(assessment)
admin.site.register(Course)
admin.site.register(Student)