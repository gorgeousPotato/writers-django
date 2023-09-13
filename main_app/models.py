from django.db import models
from django.urls import reverse

TYPES = (
  ('N', 'Novel'),
  ('S', 'Short stories collection'),
  ('P', 'Poetry collection')
)

class Writer(models.Model):
  name = models.CharField(max_length=100)
  birth_year = models.IntegerField()
  death_year = models.IntegerField()
  country = models.CharField(max_length=100)
  fav_quote = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'writer_id': self.id})
  

class Book(models.Model):
  year = models.DateField()
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
    )
  title = models.CharField(max_length=100)
  writer=models.ForeignKey(Writer, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} - {self.get_type_display()} - {self.year}"
