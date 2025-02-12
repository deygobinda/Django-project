from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import myquery

def hello_view(request):
    return HttpResponse("Hello")


def userdata(request):
    name = request.POST.get('name')
    number = request.POST.get('number')
    email = request.POST.get('email')
    print(name,number,email)
    if name != None and email != None and number != None : 
        myquery.userdatainsertion(name,email,number)
        return redirect("landing")
    return render(request , 'userform.html')


def calculator(request):
    first = request.POST.get('first')
    second = request.POST.get('second')
    d={}
    if(first != None and second != None) :
        ad = int(first) + int(second)
        d = {'x' : ad}
        print(ad)
    return render(request , 'calculator.html' , d)


def landing(request):
    return render(request , 'index.html')

def fetchuseralldata(request):
    data = myquery.userdatafetch()
    return render(request, 'table_details.html', {'users': data})


def userdataupdate(request, x):
    # Fetch user details based on ID
    user = myquery.get_user_by_id(x)  # Ensure this function exists in myquery.py
    
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        
        if name and number:
            myquery.userdataupdate(name, email, number, x)
            return redirect("fetchusers")

    return render(request, "update.html", {"user": user})

def deleteUser(request,x):
    myquery.deleteUser(x)
    return redirect('fetchusers')
   


def signin(request) : 
    e = request.session.get('email')
    print(e)
    if e is not None : 
        return  redirect('landing')

    return render(request,'signin.html')