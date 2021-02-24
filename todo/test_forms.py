from django.test import TestCase
from .forms import itemForm

# Create your tests here.


class testItemForm(TestCase):

    def test_item_name_is_required(self):
        form = itemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_what_i_want(self):
        form = itemForm()
        self.assertEqual(form.Meta.fields, ['name'])
