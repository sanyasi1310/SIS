# IMPORT THE REQUIRED FILES HERE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentInfoForm
from .models import StudentInfo, HelpDesk, Course, CourseSelection,eventbell,eventkpmg,eventwelcome, Contact
from django.contrib.auth.models import User,auth
from .forms import CreateStudentInfo, CreateCourseInfo, selectcourse, CreateHelpDesk,event_bell,event_kpmg,event_welcome, Contact_us
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView, UpdateView


# -----------HOME PAGE -----------------
def Home(request):
    return render(request, 'MTU/Home.html')
# ---- ------ABOUT PAGE -----------------
def about(request):
    return render(request, 'MTU/about.html')
# ---------FACULTY PAGE -----------------
def faculty(request):
    return render(request, 'MTU/faculty.html')
# ---------alumni PAGE -----------------
def alumni(request):
    return render(request, 'MTU/alumni.html')
# ---------FINANCE PAGE -----------------
def finance(request):
    return render(request, 'MTU/finance.html')
# ---------CAMPUS PAGE ------------------
def campus(request):
    return render(request, 'MTU/campus.html')
# ---------undergraduate PAGE -----------------
def undergraduate(request):
    return render(request, 'MTU/undergraduate.html')
# ---------graduate PAGE -----------------
def graduate(request):
    return render(request, 'MTU/graduate.html')
# ---------professionalPAGE -----------------
def professional(request):
    return render(request, 'MTU/professional.html')
# ---------CHEMICAL PAGE ------------------
def chemical(request):
    return render(request, 'MTU/chemical.html')
# ---------CIVIL PAGE ------------------
def civil(request):
    return render(request, 'MTU/civil.html')
# ---------COMPUTER PAGE ------------------
def computer(request):
    return render(request, 'MTU/computer.html')
# ---------ELECTRONICS PAGE ------------------
def electronics(request):
    return render(request, 'MTU/electronics.html')
# ---------MECHANICAL PAGE ------------------
def mechanical(request):
    return render(request, 'MTU/mechanical.html')
# ---------FAQ PAGE ------------------
def faq(request):
    return render(request, 'MTU/faq.html')
# -------MASTERPAGE PAGE ---------------------
def masterpage(request):
    request.session['username'] = request.user.username
    request.session.modified = True
    return render(request, 'MTU/masterpage.html')
# ------------Contact PAGE ------------------
def Contact_2(request):
    return render(request, 'MTU/Contact.html')
# ---------EVENT PAGE ------------------
def event(request):
    return render(request, 'MTU/event.html')

# ---------ADMISSION PAGE ------------------
def admission(request):
    return render(request, 'MTU/admission.html')

# ---------PAYMENT PAGE ------------------
def payment(request):
    return render(request, 'MTU/payment.html')

def payment_successfull(request):
    return render(request, 'MTU/payment_successfull.html')

# ----------LOGOUT__________
def logout(request):
    auth.logout(request)
    return redirect('/')
# ---------REGISTRATION PAGE ------------------
def register(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():                                                           # check weather the information is valid 
            #form.save()                                                               # if yes save and render the home-page
            userName = form.cleaned_data.get('userName')  
            firstName = form.cleaned_data.get('firstName')                            # if no render the registration page again
            password = form.cleaned_data.get('password')
            confirm = form.cleaned_data.get('confirm')
            email = form.cleaned_data.get('email')
            
            if(password == confirm):
                user = User.objects.create_user(userName, email, password)
                user.save()
                form.save()
                messages.success(request, f'Account created for {firstName}!')
                subject = "Registration on MTU Space"
                from_email = settings.EMAIL_HOST_USER
                to_email = [email]
                
                signup_message = "Thanks for registering with MTUSPACE. We are looking forward to seeing you here and sharing our inbound service with you."
                send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)
                return redirect('Home')
            else:
                form = StudentInfoForm()
                confirmP = "password doesnt match"
                return render(request, 'MTU/register.html', {'pass': confirmP, 'form': form})
    else:
        form = StudentInfoForm()
    return render(request, 'MTU/register.html', {'form': form})
# -------------LOGIN VIEW ------------
def loginview(request):
    if request.user.is_authenticated:                                                # User have to enter there authenticated username and password
        request.session['username'] = user.username
        request.session.modified = true
        return render(request, 'MTU.login1.html')

#--------HelpDesk-----------------------
def helpDesk(request):
    check = 0;
    if request.method == "POST":
        form = CreateHelpDesk(request.POST)

        if form.is_valid():
            n = form.cleaned_data["problemCategory"]
            p = form.cleaned_data["studentName"]
            z = form.cleaned_data["subCategory"]
            y = form.cleaned_data["email"]
            q = form.cleaned_data["explanation"]
            m = form.cleaned_data["department"]

            t = HelpDesk(studentId=p, problemCategory=n, subcategory=z, email=y, explanation=q, department=m)
            t.save()
            check = 1;
        else:
            form = CreateHelpDesk()
    if(check == 1):
        form = "Your request is successfully registered"
        return render(request,'MTU/HelpDesk.html', {'success': form})
    else:        
        return render(request,'MTU/HelpDesk.html')
# ---------ENROLLMENT PAGE ------------------
def Enrollment(response):
    title = "All Course"
    queryset = Course.objects.all()                                                  # User can selected there courses to enroll 
    context = {                                                                                          
        "title": title,                                                                                 
        "queryset": queryset,
    }
    return render(response, "MTU/Enrollment.html", context)
# ---------EXISITNG COURSE VIEW PAGE -----------------
def existing3(response, extra):
    title = "All Course"                                                             # As they Enroll into any of the courses
    queryset = Course.objects.all()                                                  # They can view that courses in Course section
    context = {
        "title": title,
        "queryset": queryset,
        "p": extra,
    }
    return render(response, "MTU/Enrollment.html", context)
# ---------COURSE PAGE ------------------
def course(response):
    if response.method == "POST":
        form = CreateCourseInfo(response.POST)
                                                                                      # User can view Courses and the information regarding courses 
        if form.is_valid():
            n = form.cleaned_data["name"]
            p = form.cleaned_data["code"]
            z = form.cleaned_data["faculty"]
            y = form.cleaned_data["credits"]
            q = form.cleaned_data["day"]
            m = form.cleaned_data["time"]
            o = form.cleaned_data["cost"]

            t = Course(name=n, code=p, faculty=z, credits=y, day=q, time=m, cost=o)
            t.save()

    else:
        form = CreateCourseInfo()
    return render(response, "MTU/Course.html", {"form": form})
# ---------COURSE ENROLLMENT PAGE ------------------
def viewing(response):
    queryset = {}

    title = "Course Enrollment"
    queryset = CourseSelection.objects.filter(studentId=response.user)
    total = 0
    for k in queryset:
        total += int(k.fees)

    context = {
        "title": title,
        "queryset": queryset,
        "total":total,
    }
    return render(response, "MTU/courseview.html", context)
# ---------SAVE COURSES ------------------
def savecourse(response):
    print("Values Receded")
    if response.method == "POST":
        form = selectcourse(response.POST)                                              # user select the course from the course enrollment section 
        extra = ""                                                                      # and save that information on the system
        if form.is_valid():
            print("validation")
            n = form.cleaned_data["courseName"]
            p = form.cleaned_data["studentName"]
            z = form.cleaned_data["grade"]
            y = form.cleaned_data["fees"]
            check_object = CourseSelection.objects.filter(courseId =n, studentId=p)
            print(check_object)
            if check_object.count() == 0:
                t = CourseSelection(courseId=n, studentId=p, totalGrade=z, fees=y)
                t.save()
                extra = "last course added " + n
                print("success in registration")
                return existing3(response, extra)
            else:
                extra = "Course already added."
                return existing3(response, extra)
    else:
        print("error in registration")
        return render(response, "MTU/masterpage.html")
# ---------STUDENT INFORMATION VIEW ------------------
def student_info(request):
    
    obj = StudentInfo.objects.get(userName= request.user)                             #  student/User can see there personal information 
    context = {                                                                        #  Like name, address, email, student ID
        'firstName': obj.firstName,
        'lastName': obj.lastName,
        'address': obj.address,
        'email': obj.email,
        'studentId': obj.studentId
    }
    return render (request, "MTU/student_info.html", context)
# ---------FEE CALCULATION ------------------
def finance(request):
    queryset = {}
    title = "Course Enrollment"
    queryset = CourseSelection.objects.filter(studentId=request.user)                # finance page where user get to know about the fee the have to pay
    queryset1 = StudentInfo.objects.get(userName=request.user) 
    #print(queryset1.get()
    total = 0

    for k in queryset:
        total += int(k.fees)
       
       
    context = {
        "title": title,
        "queryset": queryset,
        "queryset1": queryset1,
        "total":total,
    }
    return render(request, 'MTU/finance.html',context)

#creating the querysets to fill the forms
# creating form for registration in Event Bell
def event_bell_reg(request):
    if request.method == "POST":
        form = event_bell(request.POST)
        if form.is_valid():
            First_Name= form.cleaned_data["FirstName"]
            Last_Name = form.cleaned_data["LastName"]
            email_id = form.cleaned_data["email"]
            contact_no = form.cleaned_data["contactno"]
            print("hello")
            t = eventbell(FirstName=First_Name, LastName=Last_Name, email=email_id, contactno=contact_no)
            t.save()
            return render(request, 'MTU/event_success.html')
    else:
        print("unsuccessful")
        form = event_bell()
        return render(request, 'MTU/event_bell.html', {"form": form})

 # creating form for registration in Event KPMG   
def event_kpmg_reg(request):
    if request.method == "POST":
        form = event_kpmg(request.POST)
        if form.is_valid():
            First_Name= form.cleaned_data["FirstName"]
            Last_Name = form.cleaned_data["LastName"]
            email_id = form.cleaned_data["email"]
            contact_no = form.cleaned_data["contactno"]
            print("hello")
            t = eventkpmg(FirstName=First_Name, LastName=Last_Name, email=email_id, contactno=contact_no)
            t.save()
            return render(request, 'MTU/event_success.html')
    else:
        print("unsuccessful")
        form = event_kpmg()
        return render(request, 'MTU/event_kpmg.html', {"form": form})

# creating form for registration in Event Welcome
def event_welcome_reg(request):
    if request.method == "POST":
        form = event_welcome(request.POST)
        if form.is_valid():
            First_Name= form.cleaned_data["FirstName"]
            Last_Name = form.cleaned_data["LastName"]
            email_id = form.cleaned_data["email"]
            contact_no = form.cleaned_data["contactno"]
            print("hello")
            t = eventwelcome(FirstName=First_Name, LastName=Last_Name, email=email_id, contactno=contact_no)
            t.save()
            return render(request, 'MTU/event_success.html')
    else:
        print("unsuccessful")
        form = event_welcome()
        return render(request, 'MTU/event_welcome.html', {"form": form})

# creating form for Contact
def Contact_us_reg(request):
    check1 = 0;
    if request.method == "POST":
        form = Contact_us(request.POST)
        if form.is_valid():
            Fullname= form.cleaned_data["Fullname"]
            Phonenumber = form.cleaned_data["Phonenumber"]
            Emailaddress = form.cleaned_data["Emailaddress"]
            Message = form.cleaned_data["Message"]
            print("hello")
            t = Contact(Fullname=Fullname, Phonenumber=Phonenumber, Emailaddress=Emailaddress, Message=Message)
            t.save()
            check1=1;
    if(check1 == 1):
        form = "Your request is successfully registered"
        return render(request, 'MTU/Contact.html', {'success': form})
    else:
        print("unsuccessful")
        form = Contact_us()
        return render(request, 'MTU/Contact.html', {"form": form})