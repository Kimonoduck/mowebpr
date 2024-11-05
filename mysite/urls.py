
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token #added
urlpatterns = [
path('admin/', admin.site.urls), #a)
path('', include('blog.urls')),
path('api-token-auth/', obtain_auth_token), #added
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
