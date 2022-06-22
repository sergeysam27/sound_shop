from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from web.forms import LoginForm, RegisterForm
from web.models import Product


def index(request):
    return render(request, 'web/index.html')


def about(request):
    return render(request, 'web/about.html')


def contact(request):
    return render(request, 'web/contact.html')


def shop(request):
    return render(request, 'web/shop.html')


class ProductsListView(ListView):
    model = Product
    template_name = 'web/shop.html'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'web/product-details.html'


def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

    return render(request, 'web/login.html', context=context)


class RegisterView(TemplateView):
    template_name = 'web/register.html'


    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'web/register.html', context=context)


    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'web/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login.html')
