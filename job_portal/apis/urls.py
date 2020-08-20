from django.urls import path, include
from .views import index,error,PostList, PostDetails, UserCreate, LoginView,JobApply,UserDetails,ResumeUploadView

urlpatterns = [
    path('', index, name='index'),
    path('jobs/', PostList.as_view(), name = 'post_list'),
    path('jobs/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('jobs/<int:pk>/apply/', JobApply.as_view(), name='apply'),
    path('jobs/<int:pk>/applications/', JobApply.as_view(), name='applications'),
    path('users/', UserCreate.as_view(), name = 'user_create'),
    path('users/profile/', UserDetails.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('resume/', ResumeUploadView.as_view(),name='resumeUpload')
]
