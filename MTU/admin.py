# from.models import models
from django.contrib import admin

from.models import StudentInfo 
from.models import HelpDesk
from.models import Course
from.models import CourseSelection
from.models import eventbell
from.models import eventkpmg
from.models import eventwelcome
from.models import Contact
# Register your models here.
# admin.site.register(user info)


admin.site.register(StudentInfo)            #registering the model for the StudentInfo
admin.site.register(HelpDesk)               #registering the model for the HelpDesk
admin.site.register(Course)                 #registering the model for the Course
admin.site.register(CourseSelection)        #registering the model for the Courseselection
admin.site.register(eventbell)              #registering the model for the eventbell
admin.site.register(eventkpmg)              #registering the model for the eventkpmg
admin.site.register(eventwelcome)           #registering the model for the eventwelcome
admin.site.register(Contact)                #registering the model for the Contact