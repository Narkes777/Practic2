from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Car, Category

# Create your views here.

class CarList(ListView):
    model = Car
    context_object_name = 'car_list'
    paginate_by = 1

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

class CarDelete(DeleteView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
    template_name = 'Lesson/car_form.html'

class CategoryList(ListView):
    model = Category
    context_object_name = 'category_list'
    paginate_by = 1

class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')

class CategoryDelete(DeleteView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('category_list')
    template_name = 'Lesson/category_form.html'