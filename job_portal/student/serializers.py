from rest_framework import serializers
from .models import Student,Employer,Post,Application

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','name','username','email','phone')

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields=('id','name','username','email','phone')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('poster','profile','description','responsibilities','qualifications','experience','location')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=('applicant','post_id','resume_file_name')

