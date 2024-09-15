from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from .models import Post
from taggit.forms import TagField
from taggit.forms import TagWidget



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    tags = TagField()  # Include this field for adding/editing tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Apply TagWidget to the tags field
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
