from django.urls import path, include
from cars import views

urlpatterns = [
    path('', views.list_cars, name='cars'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact_us, name='contact'),
    path('cars/', views.list_all_cars, name='all_cars'),
    path('details/<int:pk>', views.car_details, name='car-details'),
    path('car-form/', views.car_form_view, name='car_form'),
    path("update/<int:pk>/",views.update_details,name='update_details'),
    path("delete/<int:pk>/",views.delete_car,name='delete_car'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("oauth/", include("social_django.urls", namespace='social')),
    path('register/', views.registration_view, name='register'),
    path('searchcars/', views.searchposts, name ='searchcars'),
]
