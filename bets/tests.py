from django.test import TestCase

# Create your tests here.

class BetsViewTestCase(TestCase):
    def test_list(self):
        self.assertEqual(1,1)

    def test_get_list(self):
        r = self.client.get('/api/bets')
        print(r)