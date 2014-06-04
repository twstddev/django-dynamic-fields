from django import forms
from django.template.loader import render_to_string

class RepeaterFieldWidget( forms.Widget ):
	"""
	Implements repeater widget that shows nested
	forms as a stack and allows dynamically adding
	and removing them.
	"""
	m_template = "dynamicfields/repeater_field.html"

	def __init__( self, formset, **kwargs ):
		self.formset = formset

		super( RepeaterFieldWidget, self ).__init__( kwargs )

	def render( self, name, value, attrs = None ):
		if "id" in attrs:
			self.formset.prefix = attrs[ "id" ]

		output = ""

		template_data = {
			"formset" : self.formset
		}

		output = render_to_string( self.m_template, template_data )

		return output;

	def value_from_datadict( self, data, files, name ):
		#print data
		return self.formset.__class__( data, files, prefix = name )
