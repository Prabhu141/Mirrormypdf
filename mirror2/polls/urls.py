from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('fileuploading/', views.uploadings, name='uploadings'),
    # path('pdfform/', views.pdf_upload, name='pdf_upload'),
    # path('pdf/', views.pdf180, name='pdf180'),
    # path('pdf/', views.pdf360, name='pdf360'),
    # path('pdf/', views.PdfList.as_view()),
    path('pdf/<int:pk>/', views.PdfDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)