


# Question: What are the "makemigrations" and "migrate" commands used for? Give code examples.
"""
    "makemigrations": Creates new migration files based on the changes detected in models.
        Command: python3 manage.py makemigrations
    "migrate": Applies migrations to the database.
        Command: python3 manage.py migrate        
"""

# Question: How do you rollback a migration?
"""
    Use the migrate command specifying the app name and the migration you want to rollback to.
        Command: python3 manage.py migrate app_name migration_name
"""


# Give code examples of retrieving every item in a model or just one item by its key.
"""
    all_items = ModelName.objects.all()
    single_item = ModelName.objects.get(pk=key)
"""

# How would you go about executing a specific method prior to a Model's save() method execution? Give a code example.

""" Override the save() method in the model and call the specific method before calling the parent class's save() method."""

class MyModel(models.Model):
# fields here

    def specific_method(self):
        # code here
        pass

    def save(self, *args, **kwargs):
        self.specific_method()
        super(MyModel, self).save(*args, **kwargs)
        
        
# Describe how you would construct a Model where some of the columns are dynamically defined at runtime.

"""Use a JSONField to store dynamic columns as a JSON object."""

from django.contrib.postgres.fields import JSONField

class DynamicModel(models.Model):
    # other fields here
    dynamic_columns = JSONField()
    
# Give a code example of displaying multiple Model rows in a template.

"""
    {% for item in model_items %}
      <p>{{ item.field_name }}</p>
    {% endfor %}
"""

# Give an example of referencing static resources in a template.

"""
    {% load static %}
    <img src="{% static 'img/photo.png' %}" alt="Image">
"""

# How do you ensure a View is only accessible to authenticated users? Give a code example.

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    # view logic here
    pass

# How do you validate a Form field's input before saving? Give a code example.

"""Override the clean_field_name method in the form class."""

class MyForm(forms.Form):
    # fields here

    def clean_field_name(self):
        field_data = self.cleaned_data['field_name']
        # validation logic here
        return field_data
    
# Explain what middleware is used for. Give a code example.

"""Middleware is used to process requests and responses globally before they reach the view or after they leave the view."""

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view is called
        response = self.get_response(request)
        # Code to be executed after the view is called
        return response