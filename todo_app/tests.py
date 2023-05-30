from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo


class TodoAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.todo = Todo.objects.create(title='Test Task', description='Test Task description', user=self.user)

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Task')
        self.assertEqual(self.todo.user, self.user)

    def test_todo_list_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Task')
