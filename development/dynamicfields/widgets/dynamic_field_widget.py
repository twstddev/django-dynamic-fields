from django import forms

class DynamicFieldWidget( forms.MultiWidget ):
	"""
	Implements form widget that represents multiple
	dynamic fields.
	"""

	field_template = """
	<div style="clear: both; padding: 1em 0;">
		<label for="%s" %s>%s</label>
		%s
	</div>
	<hr />
	"""
	def __init__( self, fields, **kwargs ):
		self.fields = fields

		kwargs[ "widgets" ] = [ field.field.widget for field in self.fields ]

		super( DynamicFieldWidget, self ).__init__( **kwargs )

	def decompress( self, values ):
		"""
		Gets values dictionary and makes it form widget ready.

		All what it does, just converts our dictionary back to list
		of values %).
		"""
		if values:
			return [ values[ field.name ] for field in self.fields ]
		return [ field.field.initial for field in self.fields ]

	def format_output( self, rendered_widgets ):
		output = []

		for index, field in enumerate( self.fields ):
			current_widget = rendered_widgets[ index ]

			compiled_template = self.field_template % (
				field.name,
				field.field.required,
				field.label,
				current_widget
			)
			output.append( compiled_template ) 
		return "".join( output )

