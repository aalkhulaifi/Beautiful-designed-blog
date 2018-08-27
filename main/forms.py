from django import forms
from .models import Article, Reply
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserSignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author']

        widgets = {
        	"publish_date": forms.DateInput(attrs={"type":"date"})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply']
