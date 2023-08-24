from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    path('questions/', views.questions_index, name='index'),
    path('questions/<int:question_id>', views.questions_detail, name='detail'),
    path('questions/create/', views.questions_create.as_view(), name='questions_create'),
    path('questions/update/<int:question_id>/', views.questions_update.as_view(), name="questions_update"),
    path('questions/delete/<int:question_id>/', views.questions_delete.as_view(), name="questions_delete"),
    path('questions/add_answer/<int:cat_id>/', views.add_answer, name='add_answer'),
]