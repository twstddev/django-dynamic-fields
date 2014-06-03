from django import forms

class DynamicFieldWidget( forms.MultiWidget ):
	"""
	Implements form widget that represents multiple
	dynamic fields.
	"""
