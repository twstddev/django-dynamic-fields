from django import forms
from dynamicfields.widgets import DynamicFieldWidget
from django.core.exceptions import ValidationError

class DynamicFormField( forms.MultiValueField ):
	"""
	Implements a form field that contains a list
	of fields and nested forms as well as arrays.
	"""
	def __init__( self, form, **kwargs ):
		self.form = form()

		kwargs[ "widget" ] = DynamicFieldWidget( [ field for field in self.form ] )
		kwargs[ "initial" ] = [ field.field.initial for field in self.form ]
		super( DynamicFormField, self ).__init__( **kwargs )

                self.required = False
		self.fields = [ field.field for field in self.form ]

	def compress( self, values ):
		"""
		Returns values from the form that in a dictionary.
		Basically another deserializer %)
		"""
		converted_values = {}

		if values:
			converted_values = { 
				field.name : values[ index ] 
				if not isinstance( field.field, DynamicFormField ) 
				else field.field.compress( values[ index ].values() )
				for index, field in enumerate( self.form )
			}

			validation_form = self.get_new_form_instance( converted_values )
			validation_form.is_valid()
			
			#converted_values.update( validation_form.cleaned_data )

		return converted_values

	def clean( self, values ):
		"""
		Validates nested form values and returns the validation
		result.
		"""
		return super( DynamicFormField, self ).clean( values )

	def get_new_form_instance( self, data ):
		"""
		Just returns a new instance of the specified 
		on initialization form.
		"""
		return self.form.__class__( data )
