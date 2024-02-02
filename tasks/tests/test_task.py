from rest_framework import status
from rest_framework.test import APIClient

class TestCreatTask:
    def test_if_user_anonymous_return_401(self):
        client=APIClient()
        response=client.post('/tasks/',{'title':'gym'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED