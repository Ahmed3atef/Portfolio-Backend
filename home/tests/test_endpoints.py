from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from home.models import Profile
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest


@pytest.mark.django_db
class TestProfileData:

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
