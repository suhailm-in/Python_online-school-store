from django.http import HttpResponse
from django.shortcuts import render, redirect

import storeapp.models
from .models import Person

# Create your views here.
from storeapp.models import Person


def home(request):
    return render(request,"index.html")

def order_conform(request):
    return render(request,"order_conform.html")


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']
        materials = request.POST.getlist('materials')

        print(name,phone,email,dob,age,purpose,materials,gender,address,department,courses)
        return redirect('order_conform')
    return render(request, 'form.html')



    # if request.method == 'POST':
    #     # Process the form data
    #     department = request.POST.get('department')
    #     courses = get_courses(department)
    #     return render(request, 'form.html', {'courses': courses})


# def get_courses(department):
#     if department == "commerce":
#         return ["BBA", "BCom", "MCom"]
#     elif department == "science":
#         return ["BSc", "MSc", "PhD"]
#     elif department == "arts":
#         return ["BA", "MA", "Fine Arts"]
#     else:
#         return []



# def form(request):
#     if request.method == 'POST':
#         department = request.POST.get('department')
#         courses_dropdown = []
#
#         # Add new options based on the selected department
#         if department == "commerce":
#             commerce_courses = ["BBA", "BCom", "MCom"]
#             for course in commerce_courses:
#                 option = {"text": course, "value": course}
#                 courses_dropdown.append(option)
#         elif department == "science":
#             science_courses = ["BSc", "MSc", "PhD"]
#             for course in science_courses:
#                 option = {"text": course, "value": course}
#                 courses_dropdown.append(option)
#         elif department == "arts":
#             arts_courses = ["BA", "MA", "Fine Arts"]
#             for course in arts_courses:
#                 option = {"text": course, "value": course}
#                 courses_dropdown.append(option)
#
#         context = {'courses_dropdown': courses_dropdown}
#         return render(request, 'update_courses.html', context)
#
#     # Handle GET request if needed
#     return render(request, 'form.html')







