#This are predefined forms importing from django
from django import forms
from .models import StudentInfo                         #importing student info from databse 
from django.contrib.auth.forms import UserCreationForm

#defining the field for the studentforms  
#defining the field for the studentforms  
class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['firstName','userName', 'lastName', 'address', 'email', 'studentId', 'password','confirm'] #added new username

#creating the forms for StudentInfo
class CreateStudentInfo(forms.Form):
    firstName = forms.CharField(label="FirstName", max_length=200)
    lastName = forms.CharField(label="LastName", max_length=200)
    address = forms.CharField(label="Address", max_length=200)
    email = forms.CharField(label="Email", max_length=200)
    studentId = forms.CharField(label="studentId", max_length=200)
    startDate = forms.CharField(label="StartDate", max_length=200)
    endDate = forms.CharField(label="EndDate", max_length=200)
    password = forms.CharField(label="Password", max_length=200)
    check = forms.BooleanField()

#creating the forms for CourseInfo
class CreateCourseInfo(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    code = forms.CharField(label="code", max_length=200)
    faculty = forms.CharField(label="faculty", max_length=200)
    credits = forms.CharField(label="credits", max_length=200)
    day = forms.CharField(label="day", max_length=200)
    time = forms.CharField(label="time", max_length=200)
    cost = forms.CharField(label="cost", max_length=200)
    check = forms.BooleanField()

#creating the forms for selection of course
class selectcourse(forms.Form):
    courseName = forms.CharField(label="courseName", max_length=200)
    studentName = forms.CharField(label="studentName", max_length=200)
    grade = forms.CharField(label="grade", max_length=200)
    fees = forms.CharField(label="fees", max_length=200)

#creating the forms for CreateHelpDesk
class CreateHelpDesk(forms.Form):
    problemCategory = forms.CharField(label="problemCategory", max_length=200)
    studentName = forms.CharField(label="studentName", max_length=200)
    subCategory = forms.CharField(label="subCategory", max_length=200)
    email = forms.CharField(label="email", max_length=200)
    explanation = forms.CharField(label="explanation", max_length=200)
    department = forms.CharField(label="department", max_length=200)


#creating form for event page includes the given below field
#creating the forms for event bell
class event_bell(forms.Form):
    FirstName = forms.CharField(label="FirstName", max_length=200)
    LastName = forms.CharField(label="LastName", max_length=200)
    email = forms.CharField(label="email", max_length=200)
    contactno = forms.CharField(label="contactno", max_length=200)

#creating the forms event kpmg
class event_kpmg(forms.Form):
    FirstName = forms.CharField(label="FirstName", max_length=200)
    LastName = forms.CharField(label="LastName", max_length=200)
    email = forms.CharField(label="email", max_length=200)
    contactno = forms.CharField(label="contactno", max_length=200)

#creating the forms for event welcome
class event_welcome(forms.Form):
    FirstName = forms.CharField(label="FirstName", max_length=200)
    LastName = forms.CharField(label="LastName", max_length=200)
    email = forms.CharField(label="email", max_length=200)
    contactno = forms.CharField(label="contactno", max_length=200)

#creating the forms for Contact
class Contact_us(forms.Form):
    Fullname = forms.CharField(label="Fullname", max_length=200)
    Phonenumber = forms.CharField(label="Phonenumber", max_length=200)
    Emailaddress = forms.CharField(label="Emailaddress", max_length=200)
    Message = forms.CharField(label="Message", max_length=200)