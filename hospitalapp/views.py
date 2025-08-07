from django.shortcuts import render,redirect
from hospitalapp.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'About.html')

def services(request):
    return render(request, 'services.html')

def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def Appointment(request):
    if request.method == "POST":
       myappointment = Appoint(
            name = request.POST["name"],
            email = request.POST["email"],
            phone = request.POST["phone"],
            date = request.POST["date"],
            department = request.POST["department"],
            doctor = request.POST["doctor"],
            message = request.POST["message"]
        )

       myappointment.save()
       return redirect('/')
    else:
        return render(request, 'appointment.html')


def contacts(request):
    if request.method == "POST":
        call = contact(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"],
        )

        call.save()
        return redirect('/contacts')
    else:
        return render(request, 'contacts.html')

def show(request):
     all = Appoint.objects.all()
     return render(request, 'show.html', {"all":all})



