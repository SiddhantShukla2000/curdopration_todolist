from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import user


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()  # Clear the form after saving
            add_show = "Student added successfully!" 
        else:
            add_show = "Please correct the errors below."  
        stud = user.objects.all() 
    else:
        fm = StudentRegistration()
        stud = user.objects.all()
        add_show = ""  # Default message when the form is not submitted

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud, 'add_show': add_show})

def Delete_data(request,id):
    if request.method == "POST":
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request , id):
    if request.method == "POST":
     pi = user.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
         fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request , "enroll/updatestudent.html", {'form':fm})