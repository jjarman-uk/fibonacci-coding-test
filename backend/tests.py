from django.test import TestCase
from django.urls import reverse


class FibonacciAPITest(TestCase):
    def test_get_next_fibonacci(self):

        # Test multiple Fibonacci numbers
        expected_fibonacci_numbers = ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34']
        for expected_number in expected_fibonacci_numbers:
            response = self.client.get(reverse('fibonacci'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content.decode(), expected_number)