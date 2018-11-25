from django.db import models
from django.utils import timezone


class New(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=200, null=True)
    text = models.TextField()
    type = models.CharField(max_length=20)
    public = models.CharField(max_length=20, null=True)
    display = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    source = models.CharField(max_length=200)

    # class Meta:
    #     ordering:['-pub_date']

    def __str__(self):
        return self.title
