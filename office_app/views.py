
from turtle import rt
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm, StuffForm,StuffInfoForm,StuffLogin
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps,
    }
    return render(request,'all_emp.html',context)

@login_required
def add_emp(request):
    txt = 'Add New'
    tlt = 'Add An Employee'
    link ='all_emp'
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    context = {'form':form, 'text':txt,'title':tlt,'url':link,}
    return render(request,'add_emp.html',context)
@login_required
def filter_emp(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            dept = request.POST.get('dept')
            role = request.POST.get('role')
            emps = Employee.objects.all()
            
            if name:
                emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name))
            if dept:
                emps = emps.filter(Q(department__name__icontains = dept))
            if role:
                emps = emps.filter(Q(role__name__icontains = role))

            return render(request,'all_emp.html',{'emps':emps})

        return render(request,'filter_emp.html')
@login_required
def remove_emp(request):
    object = Employee.objects.all()
    context = {
        'emps':object,
    }
    return render(request,'remove_emp.html',context)
@login_required
def confirm_emp(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        emp.delete()
        return HttpResponseRedirect(reverse('remove_emp'))

    return render(request,'confirm.html',{'emp':emp})
@login_required
def update_emp(request, id):
    txt = 'Save Changes'
    tlt = 'Edit Employee Details'
    emp = get_object_or_404(Employee, id =id)
    form = EmployeeForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('remove_emp'))
    return render(request,'add_emp.html',{'form':form,'text':txt,'title':tlt})

def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = StuffForm(request.POST)
        profile_form = StuffInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = StuffForm()
        profile_form = StuffInfoForm()
    
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered
    }

    return render(request,'registration.html',context)


def loginStuff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(email, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('all_emp'))
            else:
                return HttpResponse('Account Not Active')
        return HttpResponse('Invalid login details')

    return render(request,'login.html',{})
@login_required
def stuff_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))



    # return render(request,'login.html',{'form':user_form})