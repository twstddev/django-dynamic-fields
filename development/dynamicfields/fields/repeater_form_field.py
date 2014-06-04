from django import forms
from django.forms.formsets import formset_factory
from dynamicfields.widgets import RepeaterFieldWidget

class RepeaterFormField( forms.Field ):
	"""
	Implements a field that contains a formset
	and acts as a repeater field that allows adding and
	removing nested forms.
	"""
	def __init__( self, form, **kwargs ):
		initial = []
		initial = kwargs[ "initial" ] if "initial" in kwargs else []

		self.formset = formset_factory( form )( initial = initial, prefix = "suka" )
		kwargs[ "widget" ] = RepeaterFieldWidget( self.formset )
		self.fields = [ field for field in form()  ]

		super( RepeaterFormField, self ).__init__( **kwargs )

	def clean( self, values ):
		"""
		Returns converted to python list values.
		"""
		if values:
			converted_values = []

			# Go through every nested form
			for formset_values in values:
				# Get a dictionary of the nested form fields
				field_values = {
					field.name : formset_values[ field_index ]
					for field_index, field in enumerate( self.fields )
				}

				converted_values.append( field_values )

			return converted_values

		return values
