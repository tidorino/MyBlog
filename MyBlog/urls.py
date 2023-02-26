from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MyBlog.my_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBlog.my_blog.urls')),
    path('accounts/', include('MyBlog.accounts.urls')),
    path('articles/', include('MyBlog.articles.urls')),
]

handler404 = views.view_404
handler500 = views.view_500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
