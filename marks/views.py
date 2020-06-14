from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

# Create your views here.
from rest_framework import generics, viewsets

from .models import Result

from django.http import HttpResponse
# from rest_framework_xml.parsers import XMLParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .mark_parser import XMLParser
import numpy
from django.db.models import Min, Max, Avg, StdDev, Count, FloatField


class ResultSummary(APIView):
	def get(self, request, *args, **kwargs):

		renderer_classes = [JSONRenderer]

		test_id = kwargs.get('test_number', '1')
		count_mark = (Result.objects.filter(test_id=test_id)).count()
		min_mark = (Result.objects.filter(test_id=test_id)).aggregate(Min('mark'))
		max_mark = (Result.objects.filter(test_id=test_id)).aggregate(Max('mark'))
		mean_mark = (Result.objects.filter(test_id=test_id)).aggregate(Avg('mark'))
		std_mark = (Result.objects.filter(test_id=test_id)).aggregate(StdDev('mark'))

		results = Result.objects.filter(test_id=test_id).values('mark')
		result_array = []
		for element in results:
			result_array.append(element['mark'])
		percentile_25 = numpy.percentile(result_array, 25)
		percentile_50 = numpy.percentile(result_array, 50)
		percentile_75 = numpy.percentile(result_array, 75)
		return Response({'test_id': test_id,'count_mark':count_mark,'min_mark':min_mark, 'max_mark':max_mark, 
			'mean':mean_mark,'std_mark':std_mark, 'percentile_25':percentile_25, 'percentile_50':percentile_50, 'percentile_75':percentile_75})

class ResultPost(APIView):
	"""
	A view that can accpet Post requests with XML content
	"""
	parser_classes = [XMLParser]

	def post(self, request, format=None):
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
