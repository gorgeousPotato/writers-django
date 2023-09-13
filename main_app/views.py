from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Writer

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
  return render(request, 'writers/detail.html', {
    'writer': writer
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