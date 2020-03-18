from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('test/', views.TestView.as_view(), name='test'),
    path('test/<int:pk>', views.TestDetailView.as_view(), name='testView'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]