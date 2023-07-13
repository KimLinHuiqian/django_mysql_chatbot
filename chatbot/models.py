from django.db import models
from django.db import connection

# Create your models here.
class Citizen(models.Model):
    citizen_id = models.IntegerField(auto_created=True, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> int:
        return self.citizen_id

class Application(models.Model):
    application_id = models.IntegerField(auto_created=True, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> int:
        return self.application_id


def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row