#importing models from databse 
from django.db import models


# Create your models here.

#first model is for student info
#we have created model for student info 
#This is database for StudentInfo 
# id,firstname,lastname are the attributes for the same 
class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    studentId = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm = models.CharField(max_length=200)

    def __str__(self):
        added = self.firstName + "_" + self.lastName
        return added

#the attributes are also called as fields 
#they are the tables values for Helpdesk
class HelpDesk(models.Model):
    id = models.AutoField(max_length=200, primary_key=True)
    studentId = models.CharField(max_length=200)
    problemCategory = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        added = self.studentId
        return added

#they are the tables values for course
class Course(models.Model):
    id = models.AutoField(max_length=200, primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    credits = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#they are the tables values for course selection
class CourseSelection(models.Model):
    id = models.AutoField(max_length=200, primary_key=True, auto_created=True)
    courseId = models.CharField(max_length=200)
    studentId = models.CharField(max_length=200)
    totalGrade = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    

    def __str__(self):
        added = self.studentId + "_" + self.courseId
        return added

#they are the tables values for eventRegistration
class eventbell(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        added = self.FirstName + "_" + self.LastName
        return added

#they are the tables values for event kpmg
class eventkpmg(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        added = self.FirstName + "_" + self.LastName
        return added

#they are the tables values for event welcome
class eventwelcome(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        added = self.FirstName + "_" + self.LastName
        return added

#they are the tables values for event Contact
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=200)
    Phonenumber = models.CharField(max_length=200)
    Emailaddress = models.CharField(max_length=200)
    Message = models.CharField(max_length=200)

    def __str__(self):
        added = self.Fullname
        return added