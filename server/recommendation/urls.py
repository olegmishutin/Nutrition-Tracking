from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'recommendation'
urlpatterns = [
    path('recommendations/', login_required(views.RecommendationList.as_view()), name='recommendation-list'),
    path('diet-planning/', views.dietPlanningNutrition, name='diet-planning')
]
