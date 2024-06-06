from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recommendation, Meal
from .forms import MealForm


class RecommendationList(generic.ListView):
    model = Recommendation
    template_name = 'recommendations.html'
    context_object_name = 'recommendations'


class MealList(generic.ListView):
    model = Meal
    template_name = 'meals.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return self.request.user.meals.all()

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            photo = request.FILES.get('photo')
            mealForm = MealForm(request.POST)

            if mealForm.is_valid():
                meal = mealForm.save(commit=False)
                meal.user = self.request.user

                if photo:
                    meal.photo = photo
                meal.save()
        return super(MealList, self).get(request, *args, **kwargs)


@login_required
def dietPlanningNutrition(request):
    now_weight = request.GET.get('now_weight')
    expected_weight = request.GET.get('expected_weight')

    if now_weight and expected_weight:
        recommendations = Recommendation.objects.filter(for_current_max_weight__gte=now_weight,
                                                        for_current_min_weight__lte=now_weight,
                                                        max_expected_weight__gte=expected_weight,
                                                        min_expected_weight__lte=expected_weight)

        return render(request, 'diet_planning.html', {'recommendations': recommendations})
    return render(request, 'diet_planning.html')
