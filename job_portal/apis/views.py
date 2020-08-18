from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Posts, Applications
from .serializers import PostSerializer,UserSerializer, ApplicationSerializer

def index(request):
    return HttpResponse('Hello from django')


class PostList(APIView):
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status = 404)

class PostDetails(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCreate(generics.CreateAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({ 'token':user.auth_token.key })
        else:
            return Response({'error': 'Wrong Credentials'}, status=404)

class JobApply(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        applications = Applications.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    def post(self,request, pk, format=None):
        request.data['applicant'] = request.user.id
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(job_id=Posts.objects.get(pk=pk))
            return Response(serializer.data)
        return Response(serializer.errors, status=401)
