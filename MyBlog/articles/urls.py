from django.urls import path, include

from MyBlog.articles.views import DetailsPostView, \
    EditPostView, DeletePostView, AddPostView

urlpatterns = (
    path('add/', AddPostView.as_view(), name='add post'),

    path('post/<slug:slug>/', include([
        path('', DetailsPostView.as_view(), name='details post'),
        path('edit/', EditPostView.as_view(), name='edit post'),
        path('delete/', DeletePostView.as_view(), name='delete post'),
    ])),
)
