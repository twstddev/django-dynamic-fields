from django import forms
from django.template.loader import render_to_string

class RepeaterFieldWidget( forms.Widget ):
	"""
	Implements repeater widget that shows nested
	forms as a stack and allows dynamically adding
	and removing them.
	"""
	# This is a mostly copied admin template of stacked formset
	m_template = "dynamicfields/repeater_field.html"

	def __init__( self, formset, **kwargs ):
		self.formset = formset

		super( RepeaterFieldWidget, self ).__init__( kwargs )

	def render( self, name, value, attrs = None ):
		output = ""

		suka = self.formset( initial = value, prefix = name )

		template_data = {
			"formset" : self.formset( initial = value, prefix = name )
		}

		output = render_to_string( self.m_template, template_data )

		return output;

	def value_from_datadict( self, data, files, prefix ):
		loaded_formset = self.formset( data, files, prefix = prefix )
		loaded_formset.is_valid()
		return loaded_formset.cleaned_data
