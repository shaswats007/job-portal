from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Employer(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    def __str__(self):
        return self.name


class Post(models.Model):
    poster=models.ForeignKey(Employer,on_delete=models.CASCADE)
    profile=models.CharField(max_length=30)
    description=models.TextField(max_length=100)
    responsibilities=models.TextField(max_length=300)
    qualifications=models.TextField(max_length=300)
    experience=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    def __str__(self):
        return '%s --%s'%(self.profile,self.poster)

class Application(models.Model):
    applicant=models.ForeignKey(Student,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    resume_file_name=models.CharField(max_length=100,null=False,blank=True)
    def __str__(self):
        return self.applicant
    