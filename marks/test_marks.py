from django.test import TestCase, SimpleTestCase

# Create your tests here.
from .models import Result
from .mark_parser import XMLParser
from django.urls import include, path, reverse
import datetime
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient, APIRequestFactory
from .views import ResultPost, ResultSummary
from .urls import urlpatterns
import json
from marks_project.settings import BASE_DIR
import os
import io
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(BASE_DIR))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'marks/marks/test_files')
# class ResultModelTests(TestCase):

# 	@classmethod
# 	def setUpTestData(cls):
# 		# Create a Result
# 		testresult1 = Result.objects.create(test_id=1, scanned_on=datetime.datetime.now(),
# 			first_name='Test', last_name='Result', student_number=123, mark=75)

# 		testresult1.save()

# 	def test_result_model(self):
# 		result = Result.objects.get(id=1)
# 		min_mark = result.min_mark
# 		max_mark = result.max_mark
# 		mean_mark = result.mean_mark
# 		std_mark = result.std_mark
# 		count_mark = result.count_mark
# 		percentile_25, percentile_50, percentile_75 = result.percentiles()

# 		self.assertEqual(min_mark, 75)
# 		self.assertEqual(max_mark, 75)
# 		self.assertEqual(mean_mark, 75)
# 		self.assertEqual(std_mark, 0.0)
# 		self.assertEqual(count_mark, 1)
# 		self.assertEqual(percentile_25, 75)
# 		self.assertEqual(percentile_50, 75)
# 		self.assertEqual(percentile_75, 75)

class ResultAccessTestCase(APITestCase):
    
	def test_access_result(self):

		testresult1 = Result.objects.create(test_id=1, scanned_on=datetime.datetime.now(),
			first_name='Test', last_name='Result', student_number=123, mark=75)
		testresult1.save()
		factory = APIRequestFactory()
		request = factory.get('api/v1/1')
		view = ResultSummary.as_view()
		response = view(request, test_number=1)
		response.render()
		# self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(json.loads(response.content), {
    "test_id": 1,
    "count_mark": 1,
    "min_mark": {
        "mark__min": 75
    },
    "max_mark": {
        "mark__max": 75
    },
    "mean": {
        "mark__avg": 75
    },
    "std_mark": {
        "mark__stddev": 0.0
    },
    "percentile_25": 75,
    "percentile_50": 75,
    "percentile_75": 75
})


class ResultPostTestCase(APITestCase):

	# def setUp(self):
	# 	# with open((XMLFILES_FOLDER + '/test.xml'), 'r') as f:
	# 	# 	data = f.read()
	# 	# return data

	def test_post_result(self):
		data = io.BytesIO(XMLFILES_FOLDER + '/test.xml')
		url = '/api/v1/import/'
		factory = APIRequestFactory()
		request = factory.post(url, open(XMLFILES_FOLDER + '/test.xml'), content_type="application/xml")
		view = ResultPost.as_view()
		view(request)
		self.assertEqual(Result.objects.count(), 1)

