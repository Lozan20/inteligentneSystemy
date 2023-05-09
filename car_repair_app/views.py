from django.shortcuts import render
from .recomendations import generate_recommendations


def recommendations(request):
    """
    View function for generating and displaying recommendations for car parts.

    Args:
    request (HttpRequest): Django HTTP request object.

    Returns:
    HttpResponse: Rendered template with recommendations.
    """
    # recommendations = generate_recommendations()
    recommendations = ["Break", "Suspension","Exhaust"]
    context = {"recommendations": recommendations}
    return render(request, "car_repair_app/templates/recommendations.html", context)
