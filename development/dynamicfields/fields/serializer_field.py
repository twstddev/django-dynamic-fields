from django.db import models
import json

class SerializerField( models.Field ):
	"""
	A base class that represents a simple JSON
	field.
	"""
	__metaclass__ = models.SubfieldBase

	def db_type( self, connection ):
		"""
		Tells django what is the type of this field.
		"""
		return "text"
