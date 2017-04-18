"""visitantes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from visitantes import views

urlpatterns = [
    url(r'^$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='inicio'),
    url(r'^termos/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='termos'),
    url(r'^privacidade/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='privacidade'),
    url(r'^como-pedir/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='como-pedir'),
    url(r'^sobre-nos/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='sobre-nos'),
    url(r'^cadastre-se/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='cadastre-se'),
    url(r'^cliente-login/$', views.unica, {'plantilla': 'visitantes_entrada'},
        name='cliente-login'),
    url(r'^cadastre-seu-restaurante/$', views.unica,
        {'plantilla': 'visitantes_entrada'}, name='cadastre-seu-restaurante'),
]
