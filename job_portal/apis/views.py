from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer
from rest_framework.parsers import FileUploadParser

from .models import Posts, Applications,Resume
from .serializers import PostSerializer,UserSerializer, ApplicationSerializer

import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return HttpResponse('This is the landing page of Job Portal')

def error(request):
    return HttpResponse('You reached invalid URL')

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
        return Response(serializer.errors, status=404)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)

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



class ResumeUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = ResumeSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        all_resume=Resume.objects.all()
        serializer = ResumeSerializer(all_resume, many=True)
        return Response(serializer.data)
class JobApply(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        applications = Applications.objects.filter(job_id=pk)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    def post(self,request, pk, format=None):
        request.data['applicant'] = request.user.id
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(job_id=Posts.objects.get(pk=pk))
            return Response(serializer.data)
        return Response(serializer.errors, status=401)

class UserDetails(APIView):

    def get(self, request):
        user = CustomUser.objects.get(pk=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = CustomUser.objects.get(pk = request.user.id)
        request.data['user_type'] = user.user_type
        serializer = UserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 404)
