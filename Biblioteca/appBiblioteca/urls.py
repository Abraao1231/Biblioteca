from django.contrib import admin
from django.urls import path, include
from .views import createBook, listBooks, detailBook, updateBook


urlpatterns = [
    path('createBook', createBook),
    path('listBooks', listBooks),
    path('detailBook/<id>', detailBook),
    path('<id>', updateBook)
]
