from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recommendation


class RecommendationList(generic.ListView):
    model = Recommendation
    template_name = 'recommendations.html'
    context_object_name = 'recommendations'


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
