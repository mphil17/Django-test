from django.db import models

# Create your models here.


class item(models.Model):
    # null=false means that it won't create a todo item without a name.
    # Blank=flase is same as required
    name = models.CharField(max_length=50, null=False, blank=False)
    done_status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
