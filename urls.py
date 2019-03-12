"""react_django_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from react_django_python import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('users/', views.users),
    # path('students/', views.StudentsView.as_view()),
    # path('dog/', views.Dogview.as_view()),
    # path('admin/', admin.site.urls),
    path('api/v1/auth/$', views.AuthView.as_view()),
    path('api/v1/order/$', views.OrderView.as_view()),
]
