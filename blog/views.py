from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm,Postform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
def Home(request):
	posts = Post.objects.all()
	return render(request,'blog/home.html',{'post':posts})

def About(request):
	return render(request,'blog/about.html')


def Contact(request):
	return render(request,'blog/contact.html')

def Dashboard(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()
		form = Postform(request.POST)
		user = request.user
		full_name = user.get_full_name()
		gps = user.groups.all()
		if request.method=='POST':
			if form.is_valid():
				form.save()
				# return HttpResponseRedirect('/dashboard/')
		return render(request,'blog/dashboard.html',{'posts':posts,'form':form,'groups':gps,'full_name':full_name})
	else:
		return HttpResponseRedirect('/login/')


def Signup(request):
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			n = form.cleaned_data['username']
			print(n)
			user = form.save()
			messages.success(request, 'Account created successfully')
			group = Group.objects.get(name='author')
			user.groups.add(group)
	else:
		form = SignUpForm()
	return render(request,'blog/signup.html',{'fm':form})


def user_login(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			form = LoginForm(request=request,data=request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					messages.success(request,'you have been login successfully!!')
					return HttpResponseRedirect('/dashboard/')

		else:
			form = LoginForm()
		return render(request,'blog/login.html',{'form':form})
	else:
		return HttpResponseRedirect('/dashboard/')


def User_logout(request):
	logout(request)
	# messages.info(request, "Logged out successfully!")UPDATED
	return render(request,'blog/home.html')


def Edit_profile(request,my_id):
	pi=Post.objects.get(pk=my_id)
	form = Postform(request.POST,instance = pi)  
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/')
	else:
		pi=Post.objects.get(pk=my_id)
		form = Postform(instance=pi)
	return render(request,'blog/edit.html',{'form':form})

def Delete_profile(request,my_id):
	print(my_id)
	pi = Post.objects.get(pk=my_id)
	pi.delete()
	return HttpResponseRedirect('/dashboard/')


