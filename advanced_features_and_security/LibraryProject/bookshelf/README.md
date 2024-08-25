# Permissions and Groups Setup

## Permissions Defined:
- `can_view`: Can view book instances.
- `can_create`: Can create book instances.
- `can_edit`: Can edit book instances.
- `can_delete`: Can delete book instances.

## Groups Created:
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Enforcing Permissions in Views:
Each view is decorated with `@permission_required` to check the relevant permission before allowing access to the action.
