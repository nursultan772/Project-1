from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from django.urls import reverse_lazy


class ProductView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')



        if category:
            category_object = Category.objects.get(name=category)
            queryset = Product.objects.filter(category=category_object)
        else:
            queryset = Product.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('productView')

    def form_valid(self, form):
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('productView')

    def form_valid(self, form):
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('productView')