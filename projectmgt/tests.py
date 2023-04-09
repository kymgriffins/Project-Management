from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Project, Team, Task, Comment, Meeting
from .serializers import ProjectSerializer, TeamSerializer, TaskSerializer, CommentSerializer, MeetingSerializer
from rest_framework.test import APITestCase
from django.urls import reverse

User = get_user_model()


class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.project_data = {
            'name': 'Test Project',
            'description': 'This is a test project',
            'scope': 'Testing the functionality of the project',
            'start_date': '2022-01-01',
            'end_date': '2022-01-31',
            'status': 'inprogress',
            'current_budget': '1000.00',
            'estimated_budget': '5000.00',
            'created_by': self.user.id,
        }

        self.project = Project.objects.create(**self.project_data)

    def test_project_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_project_detail(self):
        response = self.client.get(f'/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project_data['name'])

    def test_project_create(self):
        new_project_data = {
            'name': 'New Project',
            'description': 'This is a new project',
            'scope': 'Testing the functionality of the new project',
            'start_date': '2022-02-01',
            'end_date': '2022-02-28',
            'status': 'pending',
            'current_budget': '',
            'estimated_budget': '10000.00',
            'created_by': self.user.id,
        }
        response = self.client.post('/projects/', new_project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(response.data['name'], new_project_data['name'])

    def test_project_update(self):
        updated_project_data = {
            'name': 'Updated Project',
            'status': 'completed',
        }
        response = self.client.put(f'/projects/{self.project.id}/', updated_project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, updated_project_data['name'])
        self.assertEqual(self.project.status, updated_project_data['status'])

    def test_project_delete(self):
        response = self.client.delete(f'/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)







class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(email="", password="",username="",roles=""):
        if email != "" and password != "":
            User.objects.create_user(email=email, password=password,username=username,roles=roles)

    def login_user(self, email="", password=""):
        response = self.client.post(
            reverse('token_obtain_pair'),
            data={
                "email": email,
                "password": password
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']


class ProjectTest(BaseViewTest):

    def setUp(self):
        self.create_user(email="test@test.com", password="testpass")
        token = self.login_user(email="test@test.com", password="testpass")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        self.project1 = Project.objects.create(
            name='Project 1',
            description='Description 1',
            scope='Scope 1',
            start_date='2022-01-01',
            end_date='2022-01-31',
            status='inprogress',
            current_budget=1000.00,
            estimated_budget=2000.00,
            created_by=User.objects.get(email='test@test.com'),
        )

        self.project2 = Project.objects.create(
            name='Project 2',
            description='Description 2',
            scope='Scope 2',
            start_date='2022-02-01',
            end_date='2022-02-28',
            status='pending',
            estimated_budget=3000.00,
            created_by=User.objects.get(email='test@test.com'),
        )

        self.valid_payload = {
            'name': 'Project 3',
            'description': 'Description 3',
            'scope': 'Scope 3',
            'start_date': '2022-03-01',
            'end_date': '2022-03-31',
            'status': 'completed',
            'current_budget': 1500.00,
            'estimated_budget': 3500.00,
            'created_by': User.objects.get(email='test@test.com').id,
        }

        self.invalid_payload = {
            'name': '',
            'description': 'Description 4',
            'scope': 'Scope 4',
            'start_date': '2022-04-01',
            'end_date': '2022-04-30',
            'status': 'invalid status',
            'current_budget': 'invalid budget',
            'estimated_budget': 'invalid budget',
            'created_by': 'invalid user id',
        }

    def test_get_all_projects(self):
        response = self.client.get(reverse('project-list'))
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_project(self):
        response = self.client.post(
            reverse('project-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    


    
