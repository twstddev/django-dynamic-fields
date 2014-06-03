from django import forms

class DynamicFormField( forms.MultiValueField ):
	"""
	Implements a form field that contains a list
	of fields and nested forms as well as arrays.
	"""
	def __init__( self, form, **kwargs ):
		self.form = form()

		self.fields = [ field for field in self.form ]

		super( DynamicFormField, self ).__init__( **kwargs )

	def compress( self, values ):
		"""
		Return a string represented or "compressed" value.
		"""
		pass
