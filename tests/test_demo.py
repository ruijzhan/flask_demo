import unittest
import sys
sys.path.append('.')
sys.path.append('..')

from demo import application

class DemoTestCase(unittest.TestCase):

    def setUp(self):
        application.config.update(
            TESTING = True,
            WTF_CSRF_ENABLED = False
        )
        self.client = application.test_client()
        self.runner = application.test_cli_runner()

    def tearDown(self):
        pass

    def test_app_exist(self):
        self.assertFalse(application is None)
    
    def test_app_is_testing(self):
        self.assertTrue(application.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('This is a Blueprint page', data)

if __name__ == '__main__':
    unittest.main(verbosity=2)