from django.db import models
import json

class SerializerField( models.Field ):
	"""
	A base class that represents a simple JSON
	field.
	"""
	__metaclass__ = models.SubfieldBase

	def __init__( self, *args, **kwargs ):
		"""
		Preset default and blank properties.

		It is done to avoid extra work on field
		initialization in a model.
		"""
		defaults = {
			"blank" : True,
			"default" : {},
		}
		defaults.update( kwargs )

		super( SerializerField, self ).__init__( *args, **defaults )

	def db_type( self, connection ):
		"""
		Tells django what is the type of this field.
		"""
		return "text"

	def to_python( self, value ):
		"""
		Converts the received value from a database
		to a dictionary.
		"""
		if isinstance( value, basestring ):
			return json.loads( value )

		return value

	def get_db_prep_value( self, value, **kwargs ):
		"""
		Converts database value to a dictionary.
		"""
		if isinstance( value, basestring ):
			return value
		
		return json.dumps( value )

	def value_to_string( self, instance ):
		"""
		Prepares field output for serializers.
		"""
		value = self._get_val_from_obj( instance )

		return self.get_db_prep_value( value )

try:
	from south.modelsinspector import add_introspection_rules
	add_introspection_rules( [], [ "^dynamicfields\.fields\.serializer_field\.SerializerField" ] )
except ImportError:
	pass
