from django.urls import path
#now import the views.py file into this code
from . import views
from .views import GeneratePdf

urlpatterns=[
    path('',views.index),
    path('api/contact', views.contact),
    path('api/gen-pdf', views.generate_pdf),
    # path('api/pdf', views.pdf_generation),
    # path('reports/generate/pdf/', views.get_generated_problems_in_pdf, name='pdf'),
    # path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('api/pdf', GeneratePdf.as_view()),

    path('api/business_listing', views.business_listing),
    
]
