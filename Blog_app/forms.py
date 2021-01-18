from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Blog_app.models import Comment, Sub_Comment, Profile
from django.forms import ModelForm
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        context_object_name = 'comment'


class SubCommentForm(ModelForm):
    class Meta:
        models = Sub_Comment
        fields = ['sub_comments']
        context_object_name = 'sub_comment'


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        context_object_name = 'user_profile'
        fields = ['email', 'first_name', 'last_name', 'mobile', 'gender', 'hobby', 'date_of_birth', 'linkedin',
                  'github', 'facebook', 'website', 'profile_image', 'about']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Last Name', 'class': 'form-control'}),
            'mobile': forms.TextInput(
                attrs={'placeholder': 'Contact Number', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'placeholder': 'Select', 'class': 'form-control'}),
            'hobby': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Hobby', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'linkedin': forms.URLInput(
                attrs={'type': 'url', 'placeholder': 'Link your Linkedin account', 'class': 'form-control'}),
            'github': forms.URLInput(
                attrs={'placeholder': 'Link your github account', 'class': 'form-control'}),
            'facebook': forms.URLInput(
                attrs={'placeholder': 'Link your facebook account', 'class': 'form-control'}),
            'website': forms.URLInput(
                attrs={'placeholder': 'Your website or blog', 'class': 'form-control'}),
            'profile_image': forms.FileInput(),
            'about': forms.TextInput(attrs={'type': 'text', 'placeholder': 'About', 'class': 'form-control'})
        }
