from django.shortcuts import render

def posts(request):
	return render(request, 'posts.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def Saved_Content(request):
	return render(request, 'savedcontent.html', {})

def Account(request):
	return render(request, 'account.html', {})