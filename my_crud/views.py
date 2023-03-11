from django.shortcuts import render,redirect,HttpResponse
from my_crud.models import Employee

def Index(request):
    emp=Employee.objects.all()
    context={'emp':emp}
    return render(request,"index.html",context)

def Add(request):
    if request.method == "POST":
        
       name=request.POST.get('name')
       email=request.POST.get('email')
       address=request.POST.get('address')
       phone=request.POST.get('phone')
       emp=Employee(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
    emp.save()
    return redirect('/')

def delete(request,id):
    member = Employee.objects.get(id=id)
    member.delete()
    return redirect('/')    

def update(request,id):
    member = Employee.objects.get(id=id)
    context={
        'emp':member
    }
    return render(request,"edit.html",context)

def edit(request,id):

    if request.method=="POST":
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        member = Employee.objects.get(id=id)

        member.name=name
        member.email=email
        member.address=address
        member.phone=phone

        member.save()
    return redirect('/')
 
def search(request):
    if request.method=="GET":
        data=request.GET.get('name')
        # emp=Employee.objects.filter(phone=data)
        # context={'emp':emp}
        emp=Employee.objects.all()
        res=[]
        count=0
        for i in emp:
            if i.email==data:
                res.append(i)
                count+=1
        if count==0:
            for i in emp:
                if str(i.phone)==str(data):
                    res.append(i)
        context={'emp':res}                    
        return render(request,"index.html",context)
    else:    
        return HttpResponse("Something is Wrong")
