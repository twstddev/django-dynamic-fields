from django.test import TestCase
from django import forms
from dynamicfields.fields import DynamicFormField

class CustomForm( forms.Form ):
	first = forms.CharField( max_length = 255 )
	last = forms.CharField( max_length = 255 )

class ParentForm( forms.Form ):
	field_here = forms.CharField( max_length = 255 )
	nested_form = DynamicFormField( form = CustomForm )

class DynamicFormFieldTestCase( TestCase ):
	"""
	Test main form field.
	"""
	def setUp( self ):
		self.m_data = {
			'first' : 'name',
			'last' : 'surname',
		}

		self.m_nested_data = {
			"field_here" : "some_value",
			"nested_form" : self.m_data,
		}

	def test_returns_set_values( self ):
		"""
		Makes sure that field returns supplied list
		of values.
		"""
		field = DynamicFormField( CustomForm, initial = self.m_data )
		self.assertEqual( field.clean( [ "name", "surname" ] ), self.m_data )

	def test_allows_nested_form_fields( self ):
		"""
		Makes sure that nested values are returned.
		"""
		field = DynamicFormField( ParentForm, initial = self.m_nested_data );
		self.assertEqual( field.clean( [ "somve_value", [ "name", "surname" ] ] ),  self.m_nested_data )

	def test_validates_nested_fields( self ):
		"""
		Makes sure that any nested field validates.
		"""
		form = ParentForm();
		self.assertFalse( form.is_valid() )

		form = ParentForm( self.m_nested_data )
		self.assertTrue( form.is_valid() )
