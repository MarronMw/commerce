
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
    path('customer_cart/<str:pk>', views.customer_cart,
         name="customer_cart"),  # customer_orders
    path('data/', views.submitted_data, name="data"),

    path('hello/', views.hello, name="hello"),
    path('product/<str:id>', views.checkout, name="checkout"),
    path('payment-successfull/<str:id>',
         views.payment_successful, name="success"),
    path('payment-failed/<str:id>',
         views.payment_failed, name="fail"),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
