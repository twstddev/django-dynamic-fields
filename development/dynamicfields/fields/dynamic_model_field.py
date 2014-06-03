from .serializer_field import SerializerField
from .dynamic_form_field import DynamicFormField

class DynamicModelField( SerializerField ):
	"""
	Represents a dynamic model field that specifies
	a form field to handle dynamic data.
	"""

	def __init__( self, form, *args, **kwargs ):
		self.form = form

		super( DynamicModelField, self ).__init__( *args, **kwargs )

	def formfield( self, **kwargs ):
		"""
		Just assigns a form field representation
		to the model field.

		A custom form field is used that represents
		a list of fields and accepts a form as a structure.
		"""
		defaults = {
			"form_class" : DynamicFormField,
			"form": self.form
		}
		defaults.update( kwargs )

		return super( DynamicModelField, self ).formfield( **defaults )


try:
	from south.modelinspector import add_introspection_rules
	add_introspection_rules( [], [ "^dynamicfields\.fields\.dynamic_model_field\.DynamicModelField" ] )
except ImportError:
	pass
