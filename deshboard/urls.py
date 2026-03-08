from django.urls import path, include
from .views import SummaryView, MonthlyView , CategorySummaryView


urlpatterns = [
    path('summary/', SummaryView.as_view(), name='Summary'),
    path('monthly/', MonthlyView.as_view(), name='Monthly'),
    path('category-summary/', CategorySummaryView.as_view(), name='CategorySummary'),
]
