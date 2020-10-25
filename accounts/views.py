from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from usermanagement import settings
from django.contrib import messages
from accounts.models import Profile
from django.core.mail import send_mail
from django.contrib.auth import login,logout,authenticate 
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
	return render(request,'accounts/home.html')


def aboutus(request):
	return render(request,'accounts/about.html')


def register(request):
	error=""

	if request.method=="POST":
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		uname=request.POST['username']
		em=request.POST['email']
		img=request.FILES['img']
		mb=request.POST['mobileno']
		dob=request.POST['dob']
		pwd=request.POST['pswd']
		

		try:
			user=User.objects.create_user(first_name=fname,last_name=lname,
				username=uname,email=em,password=pwd)
			Profile.objects.create(user=user,image=img,mobileno=mb,dob=dob)
			error = "no"


			res = send_mail("hello paul","comment tu vas?", "paul@polo.com", [em])
			return HttpResponse('%s'%res)

		except:
			error="yes"
	
	context={'error':error}	
	return render(request,'accounts/register.html',context)


def signin(request):
	error=""
	if request.method=="POST":
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		user=authenticate(username=uname,password=pwd)
		try:
			if user:
				login(request,user)
				error="no"
			else:
				error='yes'
		except:
			error="yes"
	context={'error':error}
	return render(request,'accounts/signin.html',context)




def signout(request):
	logout(request)
	return redirect('/')



def changepassword(request):

	error=""
	if request.method=="POST":
		o=request.POST['oldpwd']
		n=request.POST['newpwd']
		con=request.POST['conpwd']

		if n==con:


			user=User.objects.get(username__exact=request.user.username)
			user.set_password(n)
			user.save()
			error='no'


		else:
			error="yes"

	context={'error':error}


	return render(request,'accounts/changepassword.html',context)


def userprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=Profile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(request,'accounts/userprofile.html',context)




def editprofile(request):
	user=User.objects.get(id=request.user.id)
	pro=Profile.objects.get(user=user)
	error=""
	if request.method=="POST":
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		if 'img' in request.FILES:
			img=request.FILES['img']
		else:
			img=None
		mb=request.POST['mobileno']
		dob=request.POST['dob']
		user.first_name=fname
		user.last_name=lname
		pro.mobileno=mb
		pro.dob=dob
		if img:
			pro.image=img

		try:
			user.save()
			pro.save()
			error="no"
		except:
			error="yes"

	context={"error":error,'user':user,'pro':pro}
	
	
	return render(request,'accounts/editprofile.html',context)