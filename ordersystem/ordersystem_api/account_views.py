from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Account
from .serializers import AccountSerializer

class AccountDetailView(APIView):
    # add permission to check if user is authenticated
    permission_classes = []

    def get_object(self, Account_id, user_id):
        '''
        Helper method to get the object with given Account_id, and user_id
        '''
        try:
            return Account.objects.get(id=Account_id, user=user_id)
        except Account.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, Account_id, *args, **kwargs):
        '''
        Retrieves the Account with given Account_id
        '''
        Account_instance = self.get_object(Account_id, request.user.id)
        if not Account_instance:
            return Response(
                {"res": "Object with Account id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AccountSerializer(Account_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, Account_id, *args, **kwargs):
        '''
        Updates the Account item with given Account_id if exists
        '''
        Account_instance = self.get_object(Account_id, request.user.id)
        if not Account_instance:
            return Response(
                {"res": "Object with Account id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "Firstname": request.data.get("Firstname"),
            "Lastname": request.data.get("Lastname"),
            "Funds": Account_instance["Funds"] + request.data.get("Funds")
        }
        serializer = AccountSerializer(
            instance=Account_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Account_id, *args, **kwargs):
        '''
        Deletes the Account item with given Account_id if exists
        '''
        Account_instance = self.get_object(Account_id, request.user.id)
        if not Account_instance:
            return Response(
                {"res": "Object with Account id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Account_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
