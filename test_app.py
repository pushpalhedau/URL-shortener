import unittest
from app import app, get_db_connection, init_db


class URLShortenerTestCase(unittest.TestCase):

    def setUp(self):
        init_db()
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_shortening(self):
        response = self.app.post('/',
                                 data={'original_url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Short URL:', response.data)

    def test_invalid_short_url(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
