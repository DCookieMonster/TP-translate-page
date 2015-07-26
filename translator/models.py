from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
#     username=models.CharField(max_length=150,null=False,blank=False,unique=True)
#     email=models.EmailField(null=False,blank=False)
#     password=models.CharField(max_length=150,null=False,blank=False)
#     first_name=models.CharField(max_length=150,null=True,blank=True)
#     last_name=models.CharField(max_length=150,null=True,blank=True)
#     timestamp=models.DateTimeField(auto_created=True, auto_now=False)

    # def __unicode__(self):
    #     return smart_unicode(self.username)


class Paper(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    userId=models.ForeignKey(User)
    code=models.CharField(max_length=150,null=False,blank=False,unique=True)
    docx=models.FileField(blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Paragraph(models.Model):
    num=models.IntegerField(null=False,blank=False)
    paperId=models.ForeignKey(Paper)
    txt=models.TextField(null=False,blank=False)

    def __unicode__(self):
        return smart_unicode(self.num)

class Translated_Paragraph(models.Model):
    paraId=models.ForeignKey(Paragraph)
    txt=models.TextField(null=False,blank=False)

    def __unicode__(self):
        return smart_unicode(self.Id)


