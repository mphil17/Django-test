from django.test import TestCase
from .models import item

# Create your tests here.


class testViews(TestCase):

    def test_get_to_do_item(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item1 = item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item1 = item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item1.id}')
        self.assertRedirects(response, '/')
        existing_item = item.objects.filter(id=item1.id)
        self.assertEqual(len(existing_item), 0)
