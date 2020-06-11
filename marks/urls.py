from django.urls import path 

from .views import ResultSummary, ResultPost

urlpatterns = [
    path('<int:test_number>/', ResultSummary.as_view()),
    path('import/', ResultPost.as_view())
    ]