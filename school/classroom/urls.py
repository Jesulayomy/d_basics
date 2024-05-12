from django.urls import path

from classroom import views


urlpatterns = [
    path('students/', views.StudentsView.as_view(), name='students-view'),
    path('student/<int:id>/', views.StudentView.as_view(), name='student-view'),
    path('teachers/', views.TeachersView.as_view(), name='teachers-view')
]
