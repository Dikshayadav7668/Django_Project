from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home (request):
    context = {'name':'Diksha','course':'Django'}
    return render(request,'home.html',context)

def about (request):
    return render(request,'about.html') #HttpResponse ("This is my About Page (/about)")

def projects (request):
    return  render(request,'projects.html')#HttpResponse ("This is my Projects Page (/projects)")

def contact (request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name,email,phone,desc)
        ins = Contact(name = name,email= email,phone = phone,desc = desc)
        ins.save()
        print("The data is successfully saved in my database")
    return  render(request,'contact.html')#HttpResponse ("This is my Contact Page (contact)")


