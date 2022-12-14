from django.urls import path, include

from MyBlog.accounts.views import LogInUserView, RegisterUserView, LogOutUserView,\
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', LogInUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogOutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)

from .signals import *