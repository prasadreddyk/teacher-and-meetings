from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Teachers_list
from django.core.mail import send_mail
from django.conf import settings
from django.db.utils import IntegrityError

def index(request):
    return render(request,'one.html')


def home(request):
    if request.method =='POST':
        Teachername=request.POST['teachersname']
        email = request.POST['email']
        qualification = request.POST['qualification']
        subject = request.POST['subject']
        try:
            Teachers_list.objects.create(teacher_name=Teachername,email=email,qualification=qualification,subject=subject)
        except IntegrityError as err:
            return render(request, 'home.html',{"error": "try again"})
        return HttpResponse(' Your account created successfully ')
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        student_name=request.POST['data']
        request.session['data4']=student_name

        date = request.POST['date']
        request.session['sdate'] = date

        time = request.POST['time']
        request.session['stime'] = time

        link = request.POST['link']
        request.session['slink'] = link
        return HttpResponseRedirect('data')
    else:
        return render(request, 'registerappointment.html',{'name':'prasad'})


def mail(request):
    data3 = request.session['data4']
    date=request.session['sdate']
    link=request.session['slink']
    time =request.session['stime']
    return render(request,'one.html', {'data':data3,'date':date,'link':link,'time':time})

def oneTeacher(request):
    if request.method == 'POST':
        search = request.POST['srch']
        if search:
            match = Teachers_list.objects.filter(Q(teacher_name__icontains=search) | Q(email__icontains=search))
            if match:
                return render(request, "registerappointment.html", {'sr': match, })
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('teacherDetails')
    return render(request, 'registerappointment.html')


def teachersDetails(request):
        data = Teachers_list.objects.all()
        return render(request, "teacherdeatils.html", {'data': data,})
def sendmail(request):

        if request.method=="POST":
            student_name = request.POST['studentname']
            to = request.POST.get('toemail')
            date = request.POST['date']
            time = request.POST['time']
            link = request.POST['link']
            content=f"Hi mam this is {student_name}, i want fix an appointment on date :{date}, and time:{time},if this " \
                    f"time is avaliable send me ok and join in the link{link}, "\
            f" Note : As per kolkata timing this meeting is shedules"\
                .format(studentname=student_name, date=date, time=time,link=link)

            print(to,content)
            send_mail(
                #subject
            "testing",
            content,

            settings.EMAIL_HOST_USER,

            [to]
            )
            return render(
            request,'one.html'
             )
        else:
            return render(
            request,'email.html',{
            'title':'send an mail'
            }
            )

