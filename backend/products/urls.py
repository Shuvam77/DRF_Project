from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product-edit"),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('search/', views.SearchListView.as_view(), name='search'),

    # path('',views.ProductMixinView.as_view()),
    # path('<int:pk>/',views.ProductMixinView.as_view()),

    # path('<int:pk>/',views.product_alt_view),
    # path('', views.product_alt_view),


]