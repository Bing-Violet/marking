from django.test import TestCase

# Create your tests here.
from .models import Result
import datetime

class ResultTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Create a Result
		testresult1 = Result.objects.create(test_id=1, scanned_on=datetime.datetime.now(), 
			first_name='Test', last_name='Result', student_number=123, obtained=15, available=20)

		testresult1.save()

	def test_result_content(self):
		result = Result.objects.get(id=1)
		mark = result.mark
		min_mark = result.min_mark(1)

		self.assertEqual(mark, 75)
		self.assertEqual(min_mark, 75)
