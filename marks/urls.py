from django.urls import path 

from .views import ResultSummary

urlpatterns = [
    path('<int:test_number>/', ResultSummary.as_view()),
    ]