from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Person

# Create your views here.

def home(request):
    return render(request,"index.html")

def order_conform(request):
    return render(request,"order_conform.html")


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        dob = request.POST.get('dob',)
        age = request.POST.get('age',)
        gender = request.POST.get('gender',)
        phone = request.POST.get('phone',)
        email = request.POST.get('email',)
        address = request.POST.get('address',)
        department = request.POST.get('department',)
        courses = request.POST.get('courses',)
        purpose = request.POST.get('purpose',)
        materials = request.POST.getlist('materials',)

        print(name,phone,email,dob,age,purpose,materials,gender,address,department,courses)
        form=Person(name=name,dob=dob,age=age,gender=gender,phone_number=phone,mail_id=email,address=address,department=department,course=courses,purpose=purpose,materials_provided=materials)
        form.save()

        return redirect('order_conform')
    return render(request, 'form.html')




