from django.db import models
      
# Database schema

class Value(models.Model):
    value_name = models.CharField(max_length=200, null='true')

    # human-readable method for the object.
    def __str__(self):
        return self.value_name
        
    # Override table name configuration.
    class Meta:
        db_table = 'Value'

class Principle(models.Model):
    principle_name = models.CharField(max_length=200, null='true')

    # human-readable method for the object.
    def __str__(self):
        return self.principle_name

    # Override table name configuration.
    class Meta:
        db_table = 'Principle'