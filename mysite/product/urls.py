from django.urls import path
from .views import ProductView, ProductDetailView,ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", ProductView.as_view(), name='productView'),
    path("<int:pk>", ProductDetailView.as_view(), name='productDetail'),
    path("create/", ProductCreateView.as_view(), name='productCreateView'),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name='productUpdateView'),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name='productDeleteView'),
]
