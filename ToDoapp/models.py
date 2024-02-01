from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=225)
    created_date = models.DateField(auto_now_add=True, blank=True)
    user = models.CharField(max_length=225)
    options=(
        ("pending","pending"),
        ("complete","complete"),
        ("in-progress","in-progress"),
    )
    status = models.CharField(max_length=225,choices=options, default="pending")
    
    def _str_(self):
        return self.title