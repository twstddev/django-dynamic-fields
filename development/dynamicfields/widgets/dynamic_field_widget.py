from django import forms
from django.template.loader import render_to_string

class DynamicFieldWidget( forms.MultiWidget ):
	"""
	Implements form widget that represents multiple
	dynamic fields.
	"""
	m_template = "dynamicfields/dynamic_field.html"

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
			return [ values.get( field.name ) for field in self.fields ]
		return [ field.field.initial for field in self.fields ]

	def format_output( self, rendered_widgets ):
		"""
		Generates a HTML representation of dynamicformfield.
		"""
		output = "" 

		for index, field in enumerate( self.fields ):
			current_widget = rendered_widgets[ index ]

			classes = []

			if field.field.required:
				classes.append( "required" )

			template_data = {
				"label_classes" : " ".join( classes ),
				"field" : field,
				"widget" : current_widget,
			}

			output += render_to_string( self.m_template, template_data )

		return output

