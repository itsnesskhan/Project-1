from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "app/index.html")

class RegistrationView(View):
    def get(self, request):
        fm= UserRegistrationForm()
        return render(request, 'app/signup.html', {'form':fm})

    def post(self, request):
        fm= UserRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Congratulations!! User Registered Successfully!")
        return render(request, 'app/signup.html',{'form':fm})    

class SinginView(View):
    def post(self, request):
        if request.POST.get('email') and request.POST.get('password'):
            try:
                user = User.objects.get(email = request.POST.get('email'))
                if user is not None:
                    login(request,user)
                    return redirect('/')
                    messages.success(request, 'you have successfully logged in!') 
                else:
                    return render(request, 'app/signin.html',{'error':'User does not exist!'})
            except User.DoesNotExist:
                return render(request, 'app/signin.html',{'error':'Please enter correct email and passowrd!'}) 
        else:
            return render(request, 'app/signin.html',{'error':'Empty Fields!'})              
    
    def get(self, request):
        return render(request,'app/signin.html')   

def sign_out(request):
    logout(request)
    return redirect('signin')

@login_required(login_url ="signin")
def UserDetailView(request):
    users = User.objects.all()
    print(users)
    return render(request, "app/userdetail.html",{'users':users})    


def delete_data(request, id):
	ps = User.objects.get(pk =id)
	ps.delete()

	return redirect('/') 



#this fuction is used to update  data
def edit_data(request, id):
	if request.method == "POST":
		ps = User.objects.get(pk =id)
		fm = UserRegistrationForm(request.POST ,instance = ps)
		if fm.is_valid():
			fm.save()
	else:
		ps = User.objects.get(pk = id)
		fm = UserRegistrationForm(instance = ps)

	return render(request , 'app/updateuser.html', {'form':fm} )	

