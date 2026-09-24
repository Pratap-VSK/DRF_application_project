from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeeViewset, basename='employee')

urlpatterns = [   
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', views.BlogView.as_view()),
    path('comment/', views.CommentsViews.as_views),

    path('blogs/<int:pk>/', views.BlogDetailView.as_views())
    path('comments/<int:pk>/', views.CommentDetailView.as_views())



]