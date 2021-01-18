from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('tech_post/<int:id>/', views.tech_post_search, name='tech_post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('user_profile_update/<int:id>/', views.user_profile_update, name='user_profile_update'),
    path('user_profile/<int:pk>/', views.ViewUserProfile.as_view(), name='user_profile'),
    path('profile/', views.PostView.as_view(), name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    # path('comment/<int:pk>/', views.sub_comment_view, name='sub_comment'),
]
