from django.db import models
import datetime
# Create your models here.
CHOICES = (
    ('Cricket Field', 'Cricket Field'),
    ('Football Field', 'Football Field'),
    ('Badminton Court', 'Badminton Court'),
    ('Basketball Court', 'Basketball Court'),
    ('Hockey Field', 'Hockey Field'),
    ('Tennis Court', 'Tennis Court'),
    ('Athletic Field', 'Athletic Field'),
    ('Vollyball Court', 'Vollyball Court'),
)

class Field_Book(models.Model):
    name = models.CharField(max_length=128)
    roll = models.CharField(max_length=128)
    Mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    field = models.CharField(max_length= 128,
                            choices = CHOICES,
                            default = None,)
    date = models.DateField(default = datetime.date.today())
    ftime = models.TimeField()
    ttime = models.TimeField()
    status = models.CharField(max_length= 128,
                                default = 'Pending',)
    purpose = models.TextField()
