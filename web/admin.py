from django.contrib import admin
from .models import Product

# from import_export.admin import ImportExportActionModelAdmin
# from import_export import resources
# from import_export import fields 
# from import_export.widgets import ForeignKeyWidget

# class ProductResource(resources.ModelResource):
    
#     category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Product, 'name'))
#     class Meta:
#         model = Product

# class ProductAdmin (ImportExportActionModelAdmin):
#     resources_class = ProductResource
#     list_display = (field.name for field in Product._meta.field if field.name != "id")
#     inlines = (ProductImageInline)

admin.site.register(Product)