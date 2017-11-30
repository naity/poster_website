from django.db import models


# model for publications
class Abstract(models.Model):
    title = models.CharField(max_length=300)
    abstract_text = models.TextField()
    upload_datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-upload_datetime',)


class Author(models.Model):
    abstract = models.ForeignKey(Abstract, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    middle_initial = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    affiliation = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('last_name',)
