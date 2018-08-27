from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse
from .models import Article, Reply, Like
from .forms import ArticleForm, UserSignupForm, UserLoginForm, ReplyForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
	object_list = Article.objects.all().order_by('-publish_date')
	query = request.GET.get('search')
	if query:
		object_list = object_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(created__icontains=query)|
			Q(author__icontains=query)|
			Q(publish_date__icontains=query)
			).distinct()
	context = {
	"object_list": object_list,
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def signin(request):
	context = {}
	context['form'] = UserLoginForm()
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			auth_user = authenticate(username=email, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('home')
	return render(request, 'signin.html', context)



def register(request):
	form = UserSignupForm()
	if request.method=="POST":
		print ("post request")
		form = UserSignupForm(request.POST)
		if form.is_valid():
			print ("form valid")
			person = form.save(commit=False)
			person.set_password(person.password)
			person.save()

			login(request, person)
			return redirect('signin')

	print(form.errors)
	context = {
		"form":form,
	}
	return render(request, 'register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')

def create(request):
	if not request.user.is_authenticated:
		return redirect('signin')
	form = ArticleForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		article = form.save(commit=False)
		article.author=request.user
		article.save()
		return redirect("home")
	context = {
	"form": form,
	}
	return render(request, 'create.html', context)

def update(request,article_id):
	instance = Article.objects.get(id=article_id)
	form = ArticleForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect('home')
	context = {
	"form":form,
	"instance": instance,
	}
	return render(request, 'update.html', context)


def detail(request, article_id):
	instance = Article.objects.get(id=article_id)
	form = ArticleForm()

	liked = False
	if request.user.is_authenticated:
		if Like.objects.filter(article=instance, user=request.user).exists():
			liked = True
	article_like_count = Like.objects.filter(article=instance).count()

	if request.method=="POST":
		form = ReplyForm(request.POST)
		if form.is_valid():
			reply = form.save(commit=False)
			reply.article=instance
			reply.user=request.user
			reply.save()
			return redirect("detail", id=instance.id)

	replys = Reply.objects.filter(article=instance).order_by("-timestamp")

	context = {
	"replys":replys,
	"form":form,
	"instance": instance,
	"liked":liked,
	"count":article_like_count
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