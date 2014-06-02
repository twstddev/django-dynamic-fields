from django.test import TestCase
from django.db import models
from dynamicfields.fields import SerializerField

class TestModel( models.Model ):
	custom_field = SerializerField()

	class Meta:
		app_label = "dynamicfields"

custom_data = {
	"meta" : "meta_value",
	"nested" : { "nested_meta" : "nested_value" },
	"array" : [
		{
			"array_meta" : "array_value",
			"array_meta2" : "array_value2",
		}
	],
}

class SerializerFieldTestCase( TestCase ):
	"""
	Test main serializer field.
	"""
	def setUp( self ):
		self.m_test_model = TestModel.objects.create(
			custom_field = custom_data
		)

	def test_model_keeps_value( self ):
		"""
		Make sure that returned model has the specified
		dictionary.
		"""
		self.assertEqual( self.m_test_model.custom_field, custom_data )

	def test_model_saves_value_to_database( self ):
		"""
		Make sure that value gets stored to a database
		and can be retrieved back.
		"""
		retrieved_object = TestModel.objects.get( id = self.m_test_model.id )
		self.assertEqual( retrieved_object.custom_field, custom_data )

	def test_model_allows_assigning_data_after_craetion( self ):
		"""
		Make sure that meta data can be assigned after an object
		has been created.
		"""
		another_data = { "another_meta" : "another_value" }
		self.m_test_model.custom_field = another_data
		self.m_test_model.save();

		# First test that the same model has assigned value
		self.assertEqual( self.m_test_model.custom_field, another_data )

		# Now test that retrieved model from database persists the value
		retrieved_object = TestModel.objects.get( self.m_test_model.id )
		self.assertEqual( retrieved_object.custom_field, another_data )
		

