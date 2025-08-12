from django.shortcuts import render,redirect,get_object_or_404
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

def displayed(request):
    all = ward.objects.all()
    return render(request,'displayed.html', {"all":all})

def delete(request,id):
    deleteappointment= Appoint.objects.get(id = id)
    deleteappointment.delete()
    return redirect('/show')

def deleting(request,id):
    deletedisplayed= ward.objects.get(id = id)
    deletedisplayed.delete()
    return redirect('/displayed')

def edit(request,id):
    edit_appointment = get_object_or_404(Appoint, id=id)

    if request.method == "POST":
        edit_appointment.name = request.POST.get('name')
        edit_appointment.email = request.POST.get('email')
        edit_appointment.phone = request.POST.get('phone')
        edit_appointment.date = request.POST.get('date')
        edit_appointment.department = request.POST.get('department')
        edit_appointment.doctor = request.POST.get('doctor')
        edit_appointment.message = request.POST.get('message')

        edit_appointment.save()
        return redirect('/show')

    else:
        return render(request, 'edit.html', {'edit_appointment':edit_appointment})

def register(request):
    return render(request, 'register.html')

def loginview(request):
    return render(request, 'login.htmhl')




