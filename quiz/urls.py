from django.urls import path
from .views import ExamListView, ExamDetailView, ExamResultListView

app_name = 'quizzes'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('results/', ExamResultListView.as_view(), name='result_list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
]
