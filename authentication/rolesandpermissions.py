from django.contrib.auth.models import Permission
from .models import Role

# Define a list of role names and their associated permissions
roles_and_permissions = [
    {
        'role_name': 'Administrator',
        'permissions': [
            {
                'name': 'Administrator Permissions',
                'description': 'Manage user accounts and roles, access to all project data and functionality, manage system settings and configurations.'
            }
        ]
    },
    {
        'role_name': 'Project Manager',
        'permissions': [
            {
                'name': 'Project Manager Permissions',
                'description': 'Create, edit, and delete(archive) projects, assign project roles (supervisor, architect, foreman), move projects through construction phases, manage project budget and financial aspects, create, view, and edit daily records for projects, generate and manage invoices, access project reports and analytics, comment on daily records and projects.'
            }
        ]
    },
    {
        'role_name': 'Supervisor',
        'permissions': [
            {
                'name': 'Supervisor Permissions',
                'description': 'Access and view projects assigned as a supervisor, update project details (e.g., status, description) for assigned projects, create, view, and edit daily records for assigned projects, comment on daily records and projects.'
            }
        ]
    },
    {
        'role_name': 'Architect',
        'permissions': [
            {
                'name': 'Architect Permissions',
                'description': 'Access and view projects assigned as an architect, view project details and progress, access and upload project documents and blueprints, comment on daily records and projects.'
            }
        ]
    },
    {
        'role_name': 'Foreman',
        'permissions': [
            {
                'name': 'Foreman Permissions',
                'description': 'Access and view projects assigned as a foreman, view project details and progress, create, view, and edit daily records for assigned projects, comment on daily records and projects.'
            }
        ]
    },
    {
        'role_name': 'Client',
        'permissions': [
            {
                'name': 'Client Permissions',
                'description': 'View project details, progress, and reports for projects they are associated with, make online payments for projects, comment on daily records and projects.'
            }
        ]
    },
    {
        'role_name': 'Guest/Anonymous',
        'permissions': [
            {
                'name': 'Guest/Anonymous Permissions',
                'description': 'Limited access, primarily for public project information (if applicable).'
            }
        ]
    },
]

# Iterate through the roles and permissions data and create them in the database
for role_data in roles_and_permissions:
    role_name = role_data['role_name']
    permissions_data = role_data['permissions']

    # Create the Role
    role, created = Role.objects.get_or_create(name=role_name)

    # Create Permissions and associate them with the Role
    for permission_data in permissions_data:
        permission_name = permission_data['name']
        permission_description = permission_data['description']
        
        # Create Permission
        permission, created = Permission.objects.get_or_create(
            name=permission_name,
            content_type=None,
            codename=None,
            )
        permission.name = permission_name
        permission.description = permission_description
        permission.save()
        
        # Associate Permission with Role
        role.permissions.add(permission)

    print(f"Created Role: {role_name} with associated Permissions")

print("Roles and Permissions creation complete.")
