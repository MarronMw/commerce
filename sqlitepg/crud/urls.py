"""
URL configuration for sqlitepg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from . import views
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore


app_name = 'crud'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signupdata/', views.signup_submitted_data, name="signupdata"),
    path('login/', views.login, name="login"),
    path('dash/', views.dashboard, name="dashboard"),
    path('customers/<str:pk>', views.customer, name="customer"),
    path('customer_order/<str:pk>', views.customer_orders,
         name="customer_orders"),  # customer_orders
    path('hello/', views.hello, name="hello"),
    path('data/', views.submitted_data, name="data"),
    path('product/<str:id>', views.checkout, name="checkout"),
    path('payment-successfull/<str:id>',
         views.payment_successful, name="success"),
    path('payment-failed/<str:id>',
         views.payment_failed, name="fail"),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
