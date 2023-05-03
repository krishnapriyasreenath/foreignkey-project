from django.shortcuts import render,redirect
from foreignapp.models import course
from foreignapp.models import  Student

def home(request):
    return render(request,'home.html')

def add_course(request):
    return render(request,'add_course.html')

def add_coursedb(request):
    if request.method=="POST":
        course_name=request.POST.get('course')
        course_fee=request.POST.get('fee')
        cs=course(course_name=course_name,fee=course_fee)
        cs.save()
        return redirect('/')
    
def add_student(request):
    courses=course.objects.all()
    return render(request,'add_student.html',{'course':courses})

def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=course.objects.get(id=sel)
        print(course1)
        std=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        std.save()
        return redirect('/')  
def show_details(request):
    student=Student.objects.all()
    return render(request,'show_details.html',{'students':student})

def editpage(request,pk):
    std=Student.objects.get(id=pk)
    crs=course.objects.all()
    return render(request,'edit_details.html',{'Student':std,'course':crs})

def edit_student_details(request,pk):
    if request.method=="POST":
        std=Student.objects.get(id=pk)
        std.student_name=request.POST.get('name')
        std.student_address=request.POST.get('address')
        std.student_age=request.POST.get('age')
        std.joining_date=request.POST.get('jdate')
        std.save()
        return redirect('show_details')
    return render(request,"edit_details.html")

def edit_details(request):
    return render(request,'edit_details.html')


def deletepage(request,pk):
    std=Student.objects.get(id=pk)
    std.delete()     
    return redirect('show_details')     
# Create your views here.
