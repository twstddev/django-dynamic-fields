from django.contrib import admin
from dynamicfields.models import TestModel, Comment

# Register your models here.
class CommentInline( admin.StackedInline ):
	model = Comment
	extra = 0

class TestModelAdmin( admin.ModelAdmin ):
	inlines = [ CommentInline ]

admin.site.register( TestModel, TestModelAdmin )
