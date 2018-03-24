from django.shortcuts import render
from .models import Book
from django.views import generic

'''
def about(request):
    return render(request, 'books/about.html')
'''

def about(request):
    latest_question_list = Book.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'gobrother/about.html', context)

def book_list(request, posts_id):
    posts = Book.objects.get(pk=posts_id)
    return render(request, 'gobrother/book.html', {'posts': posts})
