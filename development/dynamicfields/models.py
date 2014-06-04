from django.db import models
from dynamicfields.fields import DynamicModelField, DynamicFormField
from django import forms
from django.forms.formsets import formset_factory

class SuperNestedForm( forms.Form ):
	another_nested = forms.CharField( max_length = 200 )

class NestedForm( forms.Form ):
	super_nested = forms.CharField( widget = forms.Textarea  )
	nested = DynamicFormField( SuperNestedForm )

class CustomForm( forms.Form ):
	name = forms.CharField( max_length = 200 )
	another_name = forms.CharField( max_length = 200 )
	nested_field = DynamicFormField( NestedForm )
	slides = formset_factory( SuperNestedForm, extra = 3 )

# Create your models here.
class TestModel( models.Model ):
	main_name = models.CharField( max_length = 200 )
	meta_field = DynamicModelField( form = CustomForm )
