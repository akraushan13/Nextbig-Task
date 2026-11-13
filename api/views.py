from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from rest_framework.permissions import IsAuthenticated



from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import SignupSerializers, ProductSerializer
from .models import Product

# Create your views here.


class SignupView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignupSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Register Successfully",
                             "user": serializer.data}, status=status.HTTP_201_CREATED
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)