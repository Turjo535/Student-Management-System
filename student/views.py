
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import student_model
from .forms import student_model_form

# Create your views here.
def add_student(request):
    if request.method=="POST":
        student=student_model_form(request.POST)
        if student.is_valid():
            student.save()
            messages.success(request,'Student added successfully! 🎉')
            return redirect('add')
        else:
            messages.success(request,'Error adding student. Please check the form. ❌')
    else:
        student=student_model_form()
        
    return render(request, 'add.html', {'form':student})
def display_student(request):
    student=student_model.objects.all()
    return render(request,'all_student.html',{'data':student})

def update_student(request,id):
    student=student_model.objects.get(id=id)
    print(id)
    if(request.method=='POST'):
        form=student_model_form(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Student updated successfully! ✅')
            return redirect('home')
        
        else:
            form=student_model_form(instance=student)
    return render(request,'update.html',{'student_info':student, 'form':form})

def delete(request,id):
    if(request.method=='POST'):
        student=student_model.objects.get(id=id)
        student.delete()
        messages.success(request,'Student deleted successfully! 🗑️')
        return redirect('home')