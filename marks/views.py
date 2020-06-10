from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Result
from .serializers import ResultSerializer
from django.http import HttpResponse

class ResultSummary(generics.ListAPIView):
	# def test_id(request, test_number):
	# 	return HttpResponse(test_number)
	def get_queryset(self):
		return Result.objects.filter(test_id=self.kwargs['test_number'])
	# queryset = Result.objects.filter(test_id=self.kwargs['test_number'])
	serializer_class = ResultSerializer

