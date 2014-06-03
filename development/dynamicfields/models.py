from django.db import models
from dynamicfields.fields import DynamicModelField
from django import forms

class CustomForm( forms.Form ):
	name = forms.CharField( max_length = 200 )

# Create your models here.
class TestModel( models.Model ):
	meta_field = DynamicModelField( form = CustomForm )
