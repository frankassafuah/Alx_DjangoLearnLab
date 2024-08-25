from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser
# Register your models here.


class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, AdminBook)

# Ensure the permissions are created
def create_permissions():
    content_type = ContentType.objects.get_for_model(Book)
    permissions = [
        ('can_view', 'Can view book'),
        ('can_create', 'Can create book'),
        ('can_edit', 'Can edit book'),
        ('can_delete', 'Can delete book'),
    ]
    for codename, name in permissions:
        Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

# Create groups and assign permissions
def create_groups():
    create_permissions()
    editors, created = Group.objects.get_or_create(name='Editors')
    viewers, created = Group.objects.get_or_create(name='Viewers')
    admins, created = Group.objects.get_or_create(name='Admins')

    # Assign permissions to groups
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    viewers.permissions.add(can_view)
    editors.permissions.add(can_view, can_create, can_edit)
    admins.permissions.add(can_view, can_create, can_edit, can_delete)

# Run the setup functions
create_groups()