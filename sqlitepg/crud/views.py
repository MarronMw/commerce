from django.shortcuts import render, get_object_or_404  # type: ignore
from .models import Product, Customer, Order, OrderItem
from django.http import HttpResponseRedirect  # type: ignore
from django.urls import reverse  # type: ignore
from paypal.standard.forms import PayPalPaymentsForm  # type: ignore
from django.conf import settings  # type: ignore
import uuid

# Create your views here.


def hello(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'hello.html', context)


def index(request):
    products = Product.objects.all()[::-1][:4]
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def submitted_data(request):
    email = request.POST["email"]
    pwd = request.POST["pwd"]

    if request.method == "POST":
        try:
            customers = Customer.objects.get(email=email, password=pwd)
            return customer(request, customers.customer_No)
        except (KeyError, Customer.DoesNotExist):
            return render(request, 'login.html', {

            })
    else:
        return render(request, 'login.html', {})


def signup_submitted_data(request):
    customer_name = request.POST["customer_name"]
    customer_email = request.POST["email"]
    pwd = request.POST["password"]
    pwd_confirmation = request.POST["pwd_confirm"]
    confirmation = ""
    try:

        account = Customer.objects.get(email=customer_email, password=pwd)
        confirmation = "User Already registered"
    except (Customer.DoesNotExist):

        if (pwd == pwd_confirmation):
            confirmation = "pwd afanana"
            # new customer
            registered_customer = Customer(

                customer_No=uuid.uuid4(),
                customer_name=customer_name,
                email=customer_email,
                password=pwd
            )
            # setting customer attributes

            # saving the customer
            registered_customer.save()
        else:
            confirmation = "Password doesnt match"
    finally:
        context = {
            'name': customer_name,
            'email': customer_email,
            'pwd': pwd,
            'pwd_c': pwd_confirmation,
            'confirmation': confirmation
        }
        return render(request, 'signupdata.html', context)


def dashboard(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    salesOrders = Order.objects.all()
    context = {'products': products,
               'customers': customers, 'salesOrders': salesOrders}
    return render(request, 'userDash.html', context)


# dynamic customer view
def customer(request, pk):
    customers = get_object_or_404(Customer, pk=pk)
    recent_products = Product.objects.filter().order_by('-product_No')[:3]

    context = {
        'customers': customers,
        'products': recent_products,
    }
    return render(request, 'customer.html', context)


def customer_all(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer.html', context)


def customer_orders(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    orders = customer.order_set.all()

    context = {
        'orders': orders,
        'customer': customer,
    }
    return render(request, "customer_orders.html", context)


# CHECKOUT ON PRODUCTS
def payment_successful(request, id):
    product = Product.objects.get(product_No=id)
    return render(request, "paymentSuccessfull.html", {'product': product})


def payment_failed(request, id):
    product = Product.objects.get(product_No=id)
    return render(request, "paymentFailed.html", {'product': product})


def checkout(request, id):
    product = Product.objects.get(product_No=id)

    host = request.get_host()

    # # for info given on paypal form
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product.product_name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"https://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('crud:success', kwargs={'id': product.product_No})}",
        'cancel_url': f"http://{host}{reverse('crud:fail', kwargs={'id': product.product_No})}",
    }

    # # filling the form
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        "product": product,
        "paypal": paypal_payment,
    }
    return render(request, "product.html", context)
