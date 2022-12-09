"""my_first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD

import reception
import users
=======
from users import urls

>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90

admin.site.site_header = 'Ветеринарная клиника "MOLLI"'
admin.site.index_title = 'MOLLI'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
<<<<<<< HEAD
    path('', include('users.urls'), name='user'),
    path('', include('reception.urls')),
    path('', include('users.urls'), name='register'),
    path('', include('users.urls'), name='thanks'),
    path('', include('main_page.urls'), name='main_page'),
    path('api-auth/', include('rest_framework.urls'))


=======
    path('', include(urls))
>>>>>>> 137dbcd8a0c79ac5ecc9567cbc090dc24fd17f90


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
