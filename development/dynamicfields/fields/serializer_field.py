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
		kwargs[ "default" ] = ""
		kwargs[ "blank" ] = True
		super( SerializerField, self ).__init__( *args, **kwargs )

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
			return json.load( value )

		return value
