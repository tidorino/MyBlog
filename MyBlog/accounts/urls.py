from django.urls import path, include

from MyBlog.accounts.views import LogInView, RegisterUserView, LogOutView,\
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    path('login/', LogInView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
