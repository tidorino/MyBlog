from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MyBlog.core.exception_handler import view_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBlog.my_blog.urls')),
    path('accounts/', include('MyBlog.accounts.urls')),
    path('articles/', include('MyBlog.articles.urls')),
]

# handler404 = page_not_found_view
handler500 = view_500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
