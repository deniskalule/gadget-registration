from django.db import models
from datetime import timezone, datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

category_select = (
    ('Employee', 'Employee'),
    ('Visitor', 'Visitor')
)


# creating Person/Item carrier model
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=category_select, default="In")
    organisation = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    last_update_date = models.DateTimeField(default=datetime.now, blank=True)

    last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return self.first_name


# creating Item model
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=20)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    last_update_date = models.DateTimeField(default=datetime.now, blank=True)

    last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return self.item_name


# declaring the gates of BOU in form of tuples
gate_select = (
    ('shimoni', 'Shimoni'),
    ('kampala road gate', 'KAMPALA ROAD GATE')
)
# creating ownership choices
item_owner = (
    ('Bank of Uganda', 'BANK OF UGANDA'),
    ('Personal', 'PERSONAL')
)
badge_status = (
    ('In', 'In'),
)


# creating badge in and out model
class Badge(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=gate_select, default='main gate')
    item_owner = models.CharField(max_length=20, choices=item_owner, default='Bank of Uganda')
    status = models.CharField(max_length=20, choices=badge_status, default="In")
    create_date = models.DateTimeField(default=datetime.now, blank=False)
    time_in = models.DateTimeField(default=datetime.now, blank=False)
    time_out = models.DateTimeField(default=datetime.now, blank=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    last_update_date = models.DateTimeField(auto_now=True)

    last_updated_by = models.CharField(default='admin', max_length=20)

    def __str__(self):
        return f"{self.item_name} badged in at {self.time_in}"
