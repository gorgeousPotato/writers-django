from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Writer
from .forms import BookForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def writers_index(request):
  writers = Writer.objects.all()
  return render(request, 'writers/index.html', {
    'writers': writers
  })

def writers_detail(request, writer_id):
  writer = Writer.objects.get(id=writer_id)
  book_form = BookForm()
  return render(request, 'writers/detail.html', {
    'writer': writer,
    'book_form': book_form
  })

class WriterCreate(CreateView):
  model = Writer
  fields = '__all__'
  

class WriterUpdate(UpdateView):
  model = Writer
  fields = ['birth_year', 'death_year', 'country']

class WriterDelete(DeleteView):
  model = Writer
  success_url = '/writers'

def add_book(request, writer_id):
  form = BookForm(request.POST)
  if form.is_valid():
    new_book = form.save(commit=False)
    new_book.writer_id = writer_id
    new_book.save()
  return redirect('detail', writer_id=writer_id)