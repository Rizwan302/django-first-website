from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from blog.models import Post

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request): 
    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')

def project(request):
    # messages.success(request, "Welcome to Project Page")
    return render(request,'home/project.html')


def contact(request):
    messages.success(request, 'Welcom to Contact Page')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['message']
        if len(name)<1 or len(email) < 7 or len(phone)<7 :
            messages.error(request, "Fill the Form Correcluy!")
        else:
            messages.success(request, "Form Succesfully!")

        con = Contact(name=name, email=email, phone=phone, content=content)
        con.save()
    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allpost = Post.objects.none()
            
    else:
        allposttitle = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpostauthor = Post.objects.filter(author__icontains=query)
        allpost = allposttitle.union(allpostcontent, allpostauthor)
    if allpost.count() == 0:
        messages.warning(request, 'Not search result plase enter the Value in search Box!')
    params = {'allpost':allpost, 'query':query}
    return render(request, 'home/search.html',params)



def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if len(username) > 10:
            messages.error(request, "User name Min 10 characters") 
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username ") 
            return redirect('home')
        
        if password1 != password2:
            messages.error(request, "Not match Password") 
            return redirect('home')
    
    
        myuser = User.objects.create_user(username, email, password1)
        myuser.frist_name = fname 
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account SuccessFully Created") 
        return redirect('home')
    
    else:
        return HttpResponse("Not Found")


def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username= loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "SuccessFully Login") 
            return redirect('home')
        else:
            messages.error(request, "Not Login Plase Try Again") 

            


    return HttpResponse("Not Found")

def handlelogout(request):
    
    logout(request)
    messages.success(request, "SuccessFully Logout") 
    return redirect('home')


    return HttpResponse("Logout")