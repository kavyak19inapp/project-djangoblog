
from django.contrib import admin
from django.conf.urls import url,include
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.login_redirect ,name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^chat/', include('chat.urls')),
]
