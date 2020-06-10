from django.test import TestCase

# Create your tests here.
from .models import Result
import datetime

class ResultTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Create a Result
		testresult1 = Result.objects.create(test_id=1, scanned_on=datetime.datetime.now(), 
			first_name='Test', last_name='Result', student_number=123, mark=75)

		testresult1.save()

	def test_result_model(self):
		result = Result.objects.get(id=1)
		min_mark = result.min_mark
		max_mark = result.max_mark
		mean_mark = result.mean_mark
		std_mark = result.std_mark
		count_mark = result.count_mark
		percentile_25, percentile_50, percentile_75 = result.percentiles()

		self.assertEqual(min_mark, 75)
		self.assertEqual(max_mark, 75)
		self.assertEqual(mean_mark, 75)
		self.assertEqual(std_mark, 0.0)
		self.assertEqual(count_mark, 1)
		self.assertEqual(percentile_25, 75)
		self.assertEqual(percentile_50, 75)
		self.assertEqual(percentile_75, 75)
		# self.assertEqual()

	def test_get_result(self):
		pass 
