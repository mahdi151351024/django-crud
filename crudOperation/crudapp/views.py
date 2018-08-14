from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import Employee
from django.db.models import Q


def index(request):
    all_employee = Employee.objects.all()
    search = request.GET.get('search')
    if search:
        all_employee = all_employee.filter(
            Q(name__icontains=search) |
            Q(email__contains=search) |
            Q(address__icontains=search) |
            Q(phone__icontains=search) |
            Q(designation__icontains=search)
        )
    return render(request, 'index.html', {"all_employee": all_employee})


def getcreate(request):
    if request.method=="POST":
        employee = Employee()
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.address = request.POST.get('address')
        employee.phone = request.POST.get('phone')
        employee.designation = request.POST.get('designation')
        employee.save()
        return redirect('index')
    return render(request, 'create.html')


def getupdate(request, id):
    updateEmp = get_object_or_404(Employee, id=id)
    if request.method== "POST":
        updateEmp.name =  request.POST.get('name')
        updateEmp.email = request.POST.get('email')
        updateEmp.address = request.POST.get('address')
        updateEmp.phone = request.POST.get('phone')
        updateEmp.designation = request.POST.get('designation')
        updateEmp.save()
        return redirect('index')

    return render(request, 'update.html', {"updateEmp":updateEmp})


def getdelete(request, id):
    deleteEmp = get_object_or_404(Employee, id=id)
    return render(request, 'delete.html', {"deleteEmp": deleteEmp})


def getConfirmDelete(request, id):
    deleteCEmp = get_object_or_404(Employee, id=id)
    deleteCEmp.delete()
    return redirect('index')