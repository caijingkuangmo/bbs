from django.test import TestCase

# Create your tests here.
import models

obj = models.Article(c1='xx', c2='oo')
obj.save()
