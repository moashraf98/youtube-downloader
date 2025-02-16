import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()  # Creates a test client for the Flask app

    def test_home_page(self):
        response = self.client.get('/')  # Simulate visiting home page
        self.assertEqual(response.status_code, 200)  # Expect HTTP 200 OK

    def test_invalid_url(self):
        response = self.client.post('/', data={'url': 'invalid_url'})
        self.assertEqual(response.status_code, 400)  # ✅ Expect 400 Bad Request
        self.assertIn(b'Invalid URL', response.data)  # ✅ Check if 'Invalid URL' is in response


if __name__ == '__main__':
    unittest.main()

