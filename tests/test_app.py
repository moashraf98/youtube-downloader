import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        response = self.client.post('/', data={'url': 'invalid_url'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'An error occurred', response.data)

if __name__ == '__main__':
    unittest.main()
