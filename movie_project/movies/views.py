from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from .models import Movie
from django.shortcuts import get_object_or_404


class MoviesList(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data, status=status.HTTP_418_IM_A_TEAPOT)


