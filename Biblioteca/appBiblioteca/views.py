from multiprocessing import context

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Book
from .forms import BookForms


def createBook(request):
    context = {}

    form = BookForms(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, "create_view.html", context)

def listBooks(request):
    context = {}
    context["data"] = Book.objects.all()

    return render(request, "list_books.html", context)

def detailBook(request, id):
    context = {}
    
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("Não foi encontrado nenhum livro com esse ID")
    
    context["data"] = book
    return render(request, "detail_book.html", context)

def updateBook(request, id):
    context = {}

    
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("Não foi encontrado um Livro com esse id")
    

    form = BookForms(request.POST or None, instance = book)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("detailBook/"+id)

    context["form"] = form

    return render(request, "update_book.html",context)



