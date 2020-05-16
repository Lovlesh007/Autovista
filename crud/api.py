from crud.models import Crud
from rest_framework import viewsets,permissions
from .serializers import CrudSerializer


#Now need to crate a view sets( IT GOONA HELPS TO PERFORM THE FULL CRUD OPERATIONS) without explicit function and routes

class CrudViewSet(viewsets.ModelViewSet):
	queryset=Crud.objects.all()  
	permission_classes=[ 
	permissions.AllowAny
	]

	serializer_class= CrudSerializer

