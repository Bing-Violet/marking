from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets

from .models import Result
from .serializers import ResultSerializer
from django.http import HttpResponse
# from rest_framework_xml.parsers import XMLParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .mark_parser import XMLParser
import numpy


class ResultSummary(generics.ListAPIView):
	# def test_id(request, test_number):
	# 	return HttpResponse(test_number)
	# serializer_class = ResultSerializer

	# def get_queryset(self):
	# 	return Result.objects.filter(test_id=self.kwargs['test_number'])
	# 	results = filtered.values('mark')
	# 	result_array = []
	# 	for element in results:
	# 		result_array.append(element['mark'])
	# 	percentile_25 = numpy.percentile(result_array, 25)
	# 	percentile_50 = numpy.percentile(result_array, 50)
	# 	percentile_75 = numpy.percentile(result_array, 75)
	# 	return percentile_25, percentile_50, percentile_75

	# def min_mark(self):
	# 	return (filtered.aggregate(min_mark=Min('mark')))['min_mark']
	# def max_mark(self):
	# 	return (filtered.aggregate(max_mark=Max('mark')))['max_mark']
	# def mean_mark(self):
	# 	return (filtered.aggregate(avg_mark=Avg('mark')))['avg_mark']
	# def std_mark(self):
	# 	return (filtered.aggregate(std_mark=StdDev('mark')))['std_mark']
	# def count_mark(self):
	# 	return (filtered.aggregate(count_mark=Count('mark')))['count_mark']
	def get_queryset(self):
		return Result.objects.filter(test_id=self.kwargs['test_number'])
	# queryset = Result.objects.filter(test_id=self.kwargs['test_number'])
	serializer_class = ResultSerializer

class ResultPost(APIView):
	"""
	A view that can accpet Post requests with XML content
	"""
	parser_classes = [XMLParser]

	def post(self, request, format=None):
		# return Response({'received data': request.data})
		test_id = request.data[0]['mcq-test-result']['test-id']
		# scanned_on = request.data[1]['scanned_on']
		first_name = request.data[0]['mcq-test-result']['first-name']
		last_name = request.data[0]['mcq-test-result']['last-name']
		student_number = request.data[0]['mcq-test-result']['student-number']
		mark = request.data[2]['summary-marks']
		if Result.objects.filter(student_number=student_number).count() != 0 and Result.objects.filter(student_number=student_number)[0].mark > mark:
			pass
		else:
			Result.objects.filter(student_number=student_number).delete()
			self.save_record(test_id, first_name, last_name, student_number, mark)

	def save_record(self, test_id, first_name, last_name, student_number, mark):
		new_record = Result.objects.create(test_id = test_id, first_name=first_name, last_name=last_name, student_number=student_number, mark=mark)
		new_record.save()

# class ResultPost(generics.ListCreateAPIView):
# 	queryset = Result.objects.all()
# 	parser_classes = (XMLParser)
