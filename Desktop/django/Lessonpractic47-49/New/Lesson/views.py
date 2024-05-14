from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car, Category

# Create your views here.

class CarList(LoginRequiredMixin, ListView):
    model = Car
    context_object_name = 'car_list'
    paginate_by = 3
    paginate_orphans = 2

class CarDetail(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = 'car'

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'Lesson/car_form.html'

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'category_list'
    paginate_by = 1

class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    context_object_name = 'category'

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')
    template_name = 'Lesson/category_form.html'

class CarLogoutView(LogoutView):
    pass

class CarLoginView(LoginView):
    template_name = 'Lesson/login.html'

