"""point URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home, name='home'),
    url(r'^user$', home_views.user, name='user'),
    url(r'^waitlist$', home_views.waitlist, name='waitlist'),
    url(r'^appointments$', home_views.appointments, name='appointments'),
    url(r'^calendar$', home_views.calendar, name='calendar'),

    # INICIO URLS LISTAS (BORRAR DESPUÉS)
    url(r'^cardiologia$', home_views.cardiologia, name='cardiologia'),
    url(r'^traumatologia$', home_views.traumatologia, name='traumatologia'),
    url(r'^urologia$', home_views.urologia, name='urologia'),
    url(r'^todas$', home_views.todas, name='todas'),
    # TERMINO URL LISTAS (BORRAR DESPUÉS)
]
