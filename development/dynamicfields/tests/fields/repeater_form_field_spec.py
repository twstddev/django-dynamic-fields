from django.test import TestCase
from django import forms
from dynamicfields.fields import RepeaterFormField

class CustomForm( forms.Form ):
	first = forms.CharField( max_length = 200 )
	second = forms.CharField( max_length = 200 )

class ParentForm( forms.Form ):
	nested = RepeaterFormField( CustomForm )

class RepeaterFormFieldTestCase( TestCase ):
	"""
	Test repeater form field.
	"""
	def setUp( self ):
		self.m_data = [
			{
				"first" : "value",
				"second" : "value2",
			},
			{
				"first" : "value3",
				"second" : "value4",
			},
		]

	def test_returns_set_values( self ):
		"""
		Makes sure that field returns supplied values in
		a form of a list.
		"""
		field = RepeaterFormField( CustomForm, initial = self.m_data )
		self.assertEqual( field.clean( [ [ "value", "value2" ], [ "value3", "value4" ] ] ), self.m_data )

	def test_validates_nested_fields( self ):
		"""
		Checks if field can validate provided values.
		"""
		form = ParentForm()
		self.assertFalse( form.is_valid() )

		form = ParentForm( {
			"nested-0-first" : "value",
			"nested-1-first" : "value2",
			"nested-2-first" : "value3",
			"nested-3-first" : "value4",
		} );
		self.assertTrue( form.is_bound )
		self.assertTrue( form.is_valid() )
