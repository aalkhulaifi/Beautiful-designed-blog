from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse
from .models import Article, Reply, Like
from .forms import ArticleForm, UserRegisterForm, SigninForm, ReplyForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
	context = {
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def signin(request):
	context = {
	}
	return render(request, 'signin.html',context)

def register(request):
	context = {
	}
	return render(request, 'register.html',context)

def user_logout(request):
	logout(request)
	return redirect('signin')

def create(request):
	context = {
	}
	return render(request, 'create.html', context)

def update(request):
	context = {
	}
	return render(request, 'update.html', context)


def detail(request, pk):
	context = {

	}
	return render(request, 'detail.html', context)

def likes(request, article_id):
	article = article.objects.get(id=article_id)

	impressed, created = Like.objects.get_or_create(user=request.user, article=article)
	if created:
		action="like"
	else:
		action="unlike"
		impressed.delete()

	article_like_count = Like.objects.filter(article=article).count()

	context = {
		"action":action,
		"count":article_like_count
	}
	return JsonResponse(context, safe=False)


def delete(request, article_id):
	Article.objects.get(id=article_id).delete()
	return redirect("home")