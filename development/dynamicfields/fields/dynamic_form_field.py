from django import forms

class DynamicFormField( forms.MultiValueField ):
	"""
	Implements a form field that contains a list
	of fields and nested forms as well as arrays.
	"""
	def __init__( self, form, **kwargs ):
		self.form = form()

		kwargs[ "initial" ] = [ field.field.initial for field in self.form ]
		super( DynamicFormField, self ).__init__( **kwargs )

		self.fields = [ field.field for field in self.form ]

	def compress( self, values ):
		"""
		Returns a dictionary prepared set of values.
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

			return validation_form.cleaned_data

		return converted_values

	def get_new_form_instance( self, data ):
		"""
		Just returns a new instance of the specified 
		on initialization form.
		"""
		return self.form.__class__( data )
