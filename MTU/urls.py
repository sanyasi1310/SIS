from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views

# URL of all webpages in your app.

urlpatterns = [
    path('admission', views.admission, name='admission'),
    path('Contact', views.Contact_2, name='Contact'),
    path('masterpage', views.masterpage, name='masterpage'),
    path('', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('faculty', views.faculty, name='faculty'),
    path('campus', views.campus, name='campus'),
    path("Course/", views.Course, name="Course"),
    path("Enrollment/", views.Enrollment, name="Enrollment"),
    path("savecourse/", views.savecourse, name="savecourse"),
    path('HelpDesk/',views.helpDesk,name='HelpDesk'),
    path('event', views.event, name='event'),
    path('student_info', views.student_info, name='student_info'),
    path('displaycourse', views.viewing, name='displaycourse'),
    path('finance', views.finance, name='finance'),
    path('faq', views.faq, name='faq'),
    path('civil', views.civil, name='civil'),
    path('chemical', views.chemical, name='chemical'),
    path('computer', views.computer, name='computer'),
    path('electronics', views.electronics, name='electronics'),
    path('mechanical/', views.mechanical, name='mechanical'),
    path('payment/', views.payment, name='payment'),
    path('payment_successfull/', views.payment_successfull, name='payment_successfull'),
    url(r'^logout/', views.logout, name='logout'),
    path('event_bell/',views.event_bell_reg,name='event_bell'),
    path('event_kpmg/',views.event_kpmg_reg,name='event_kpmg'),
    path('event_welcome/',views.event_welcome_reg,name='event_welcome'),
    path('Contact_us/',views.Contact_us_reg,name='Contact_us'),
    path('alumni/',views.alumni,name='alumni'),
    path('undergraduate/',views.undergraduate,name='undergraduate'),
    path('graduate/',views.graduate,name='graduate'),
    path('professional/',views.professional,name='professional'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='MTU/password-reset/password_reset.html',
             subject_template_name='MTU/password-reset/password_reset_subject.txt',
             email_template_name='MTU/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='MTU/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='MTU/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='MTU/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]