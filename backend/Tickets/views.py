from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from Tickets.models import User
from Tickets.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

    # def get_object(self):
    #     user_id = self.kwargs.get('user_id')
    #     try:
    #         return User.objects.get(id=user_id)
    #     except User.DoesNotExist:
    #         raise NotFound(detail="User not found", code=404)
