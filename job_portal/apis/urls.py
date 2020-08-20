from django.urls import path, include
from .views import index,PostList, PostDetails, UserCreate, LoginView,ResumeUploadView

urlpatterns = [
    path('', index, name='index'),
    path('jobs/', PostList.as_view(), name = 'post_list'),
    path('jobs/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('users/', UserCreate.as_view(), name = 'user_create'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('resume/', ResumeUploadView.as_view(),name='resumeUpload')
]