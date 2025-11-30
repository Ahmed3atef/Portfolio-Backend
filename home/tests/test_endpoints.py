import os
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from home.models import Profile, SkillCategory, Skill, Experience, Project, Reward


@pytest.mark.django_db
class TestProfileDataAPI:

   def setup_method(self, method):
      self.client = APIClient()
      User = get_user_model()

      if method.__name__ != 'test_get_profile_no_data_returns_404':
         # Create mock file content for FileFields
         self.dummy_image_content = SimpleUploadedFile(
            "dummy_image.jpg",
            b"file_content",
            content_type="image/jpeg"
         )
         self.dummy_cv_content = SimpleUploadedFile(
            "dummy_cv.pdf",
            b"pdf_content",
            content_type="application/pdf"
         )

         # 2. Create the Required User Object
         self.user_data = {
            'username': 'main_profile_user',
            'password': 'testpassword123',
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
         }

         # 3. Create the Required Profile Object Data
         self.profile_data = {
            # Create user linked here
            'user': User.objects.create_user(**self.user_data),
            'title': 'Software Engineer',
            'image': self.dummy_image_content,
            'description': 'A passionate developer.',
            'phone': '(555) 123-4567',
            'location': 'San Francisco, CA',
            'facebook_url': 'https://facebook.com/johndoe',
            'github_url': 'https://github.com/johndoe',
            'instagram_url': 'https://instagram.com/johndoe',
            'linkedin_url': 'https://linkedin.com/in/johndoe',
            'cv': self.dummy_cv_content,
            'game_url': 'https://johndoe.itch.io/'
         }

         self.profile = Profile.objects.create(**self.profile_data)

   def test_get_profile_no_data_returns_404(self):
        # ARRANGE: The database is empty because data creation was skipped in setup_method.
        url = reverse('profile-list')

        # ACT
        response = self.client.get(url)

        # ASSERT
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()['detail'] == "No profiles found."

   def test_get_profile_data_returns_200_and_correct_data(self):
      # ARRANGE: Data is already created in setup_method. URL is reversed.
      url = reverse('profile-list')

      # ACT
      response = self.client.get(url)

      # ASSERT
      assert response.status_code == status.HTTP_200_OK

      # Verify a few fields in the response data
      assert response.data['title'] == 'Software Engineer'
      assert response.data['name'] == 'John Doe'


@pytest.mark.django_db
class TestSkillsAPI:

   def setup_method(self, method):
      self.client = APIClient()

      # 1. Create Categories
      self.cat_lang = SkillCategory.objects.create(title="Languages")
      self.cat_frame = SkillCategory.objects.create(title="Frameworks")

      # 2. Create Skills linked to Categories
      Skill.objects.create(category=self.cat_lang, name="Python")
      Skill.objects.create(category=self.cat_lang, name="Go")
      Skill.objects.create(category=self.cat_frame, name="Django")

   def test_get_skills_returns_nested_structure(self):
       """
        Verifies that the API returns a list of categories,
        and each category contains a list of skill names (strings) in 'items'.
        """
       url = reverse("skillcategory-list")
       response = self.client.get(url)

       assert response.status_code == status.HTTP_200_OK

       # Verify it returns a list
       assert isinstance(response.data, list)
       assert len(response.data) == 2

       # Check structure of the first object (Languages)
       lang_data = next(
           item for item in response.data if item["title"] == "Languages")

       # CRITICAL: Verify 'items' is a list of strings, not objects
       assert "items" in lang_data
       assert isinstance(lang_data['items'], list)
       assert "Python" in lang_data['items']
       assert "Go" in lang_data['items']

       # Check structure of second object
       frame_data = next(
           item for item in response.data if item["title"] == "Frameworks")
       assert "Django" in frame_data['items']


@pytest.mark.django_db
class TestExperienceAPI:

   def setup_method(self, method):
      self.client = APIClient()

      # Create dummy experience
      self.exp1 = Experience.objects.create(
          title="Senior Backend Engineer",
          company="Tech Corp",
          start_date="2023-01-01",
          end_date=None,
          location="New York, NY",
          tasks=["Designed microservice architecture.",
                   "Improved API latency."]
         )

   def test_get_experience_returns_list_of_tasks(self):
         """
         Verifies that the 'tasks' field is returned as an Array of Strings.
         """
         url=reverse("experience-list")
         response=self.client.get(url)

         assert response.status_code == status.HTTP_200_OK
         assert isinstance(response.data, list)

         item=response.data[0]

         assert item['title'] == "Senior Backend Engineer"
         assert item['company'] == "Tech Corp"

         # Verify 'tasks' is a list/array
         assert isinstance(item['tasks'], list)
         assert len(item['tasks']) == 2
         assert item['tasks'][0] == "Designed microservice architecture."

@ pytest.mark.django_db
class TestProjectsAPI:
   def setup_method(self, method):
      self.client=APIClient()
      image_file = SimpleUploadedFile(
          "project.jpg", b"image_content", content_type="image/jpeg"
      )

      self.project = Project.objects.create(
          title="Project Alpha",
          description="A microservice e-commerce backend.",
          image=image_file,
          source_link="https://github.com/user/alpha",
          demo_link="https://alpha-demo.com"
      )

   def test_get_projects_returns_correct_fields_and_image_url(self):
       url = reverse("project-list")
       response = self.client.get(url)

       assert response.status_code == status.HTTP_200_OK
       item = response.data[0]

       assert item['title'] == "Project Alpha"

       assert 'source_url' in item
       assert item['source_url'] == "https://github.com/user/alpha"

       assert 'demo_url' in item
       assert item['demo_url'] == "https://alpha-demo.com"

       assert 'image_url' in item
       assert item['image_url'].startswith('http')

       db_filename = os.path.basename(self.project.image.name)

       assert db_filename in item['image_url']

@ pytest.mark.django_db
class TestRewardsAPI:

   def setup_method(self, method):
      self.client=APIClient()
      
      image_file = SimpleUploadedFile(
          "award.png", b"image_content", content_type="image/png"
      )

      self.reward = Reward.objects.create(
          title="AWS Certified Developer",
          description="Expertise in cloud.",
          image=image_file,
          link="https://aws.amazon.com/verify/123"
      )

   def test_get_rewards_returns_correct_json_keys(self):
       url = reverse("reward-list")
       response = self.client.get(url)

       assert response.status_code == status.HTTP_200_OK
       item = response.data[0]

       assert item['title'] == "AWS Certified Developer"

       assert 'credential_url' in item
       assert item['credential_url'] == "https://aws.amazon.com/verify/123"

       assert 'image_url' in item
       assert item['image_url'].startswith('http')
