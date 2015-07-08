import unittest

from django_choices_enum import ChoicesEnum

class Status(ChoicesEnum):
    READY = (1, 'Label Ready')
    WILLING = (2, 'Label Willing')

class IntStatus(int, ChoicesEnum):
    READY = (1, 'Label Ready')
    WILLING = (2, 'Label Willing')

class StrStatus(str, ChoicesEnum):
    READY = ('value ready', u'Label Ready')
    WILLING = ('value willing', u'Label Willing')

class BasicTest(unittest.TestCase):

    def test_simple_enums(self):
        self.assertEqual(Status.READY, Status(1))
        self.assertNotEqual(Status.WILLING, 2)

    def test_int_enums(self):
        self.assertEqual(IntStatus.READY, 1)

    def test_str_enums(self):
        self.assertEqual(StrStatus.WILLING, 'value willing')
        self.assertNotEqual(StrStatus.WILLING, 'Label Willing')

    def test_iterable(self):
        for value, label in IntStatus:
            self.assertIsInstance(value, int)
            self.assertIsInstance(label, basestring)
            self.assertTrue(label.startswith('Label'))

        for value, label in StrStatus:
            self.assertIsInstance(value, str)
            self.assertTrue(value.startswith('value'))
            self.assertIsInstance(label, basestring)
            self.assertTrue(label.startswith('Label'))

        for value, label in Status:
            self.assertIsInstance(value, int)
            self.assertIsInstance(label, basestring)
            self.assertTrue(label.startswith('Label'))
