from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription (
            name = 'Fernando Queiroz',
            cpf = '12345678901',
            email = 'flcavqueiroz@gmail.com',
            phone = '11-985117980'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        '''Subscription must have an auto created_at attr.'''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Fernando Queiroz', str(self.obj))
    