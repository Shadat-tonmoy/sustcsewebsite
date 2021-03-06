from django.db import models
from curriculum.models import Program, Semester
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Notice(models.Model):
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500)
    details = models.TextField(blank=True, null=True)
    date_published = models.DateField(auto_now_add=True)
    upload = models.FileField(blank=True, null=True, upload_to='notices/%Y/%m/%d/')

    def __str__(self):
        return self.title


class HonorBoard(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    details = RichTextField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=500)
    date_published = models.DateField(auto_now_add=True)
    details = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "news"


class Event(models.Model):
    title = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=500)
    details = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title



