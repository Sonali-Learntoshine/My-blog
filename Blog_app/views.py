from .models import Post, Profile, Comment, Technology, MyIntroduction, InterestingCorner
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from .forms import SignupForm, UserProfileForm
from django.contrib import messages


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            return redirect('login')
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + username)
            return redirect('login')
        else:
            messages.error(request, 'Please Enter valid credentials')
            return redirect('signup')
    return render(request, 'Blog_app/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'successfully logged in')
                return redirect('index')
            else:
                messages.error(request, 'Incorrect Username or Password')
    return redirect('registration/login')


class PostView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['popular_post'] = Post.objects.all().order_by('-id')[:5]
        context['technology'] = Technology.objects.all()
        context['introduction'] = MyIntroduction.objects.all()
        context['interesting_corner'] = InterestingCorner.objects.all()
        return context


def tech_post_search(request, id):
    obj = Technology.objects.get(id=id)
    post = Post.objects.filter(technology_used=obj)
    return render(request, 'Blog_app/tech_post.html', {'post': post,
                                                       'obj': obj})


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post_detail'

    def get_object(self, queryset=None):
        obj = super(PostDetail, self).get_object()
        obj.post_view += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            messages.error(request, 'Please Login')
            print(request.user.is_authenticated)
            if not request.user.is_authenticated:
                return redirect('login')
            else:
                obj_ = super(PostDetail, self).get_object()
                data = Comment(post=obj_, user_name=Profile.objects.get(username=request.user),
                               comment=request.POST['comment'])
                messages.success(request, 'U commented on this post')
                data.save()
                return redirect('post_detail', obj_.pk)


def user_profile_update(request, id):
    instance = get_object_or_404(Profile, id=id)
    form = UserProfileForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        # print(form.is_valid())
        # print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('index')
        else:
            print(form.errors)
            messages.error(request, 'Please fill the form')

    context = {
        'form': form,
        'user': instance,
    }
    return render(request, 'Blog_app/user_profile_update.html', context)


class ViewUserProfile(DetailView):
    model = Profile
    template_name = 'Blog_app/view_user_profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return Profile.objects.get(id=self.kwargs.get('pk'))


# def sub_comment_view(request, *args, **kwargs):
#     if request.method == Post:
#         form = SubCommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
#             new_comment.user_name = request.user
#             new_comment.save()
#             messages.success(request, "You commented on this post")
#             return redirect('post_detail')
#     else:
#         form = SubCommentForm()
#     return render(request, 'Blog_app/sub_comment.html', {'form': form})


'''
def change_password(request):
    form = PasswordChangeForm(None)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed')
            return redirect('teacher:view_course')
        else:
            messages.error(request, 'Be sure about the credentials')

    return render(request, 'Blog_app/change_password.html', {'form': form})


'''
