package accesscontrol

# Define roles and the resources and actions they can access
roles = {
    "admin": [{"resource": "*", "action": "*"}],
    "editor": [{"resource": "documents", "action": "read"}, {"resource": "documents", "action": "write"}],
    "viewer": [{"resource": "documents", "action": "read"}]
}

# Check if a user has permission to perform an action on a resource
allow {
    # Retrieve the user's role, resource, and action from the input
    user_role := input.user.role
    resource := input.resource
    action := input.action

    # Get the permissions for the user's role
    permissions := roles[user_role]

    # Check if the user has the required permission
    permission := {"resource": resource, "action": action}
    permission_in_permissions(permission, permissions)
}

# Helper rule to check if a permission is in a list of permissions
permission_in_permissions(permission, permissions) {
    perm := permissions[_]
    perm.resource == permission.resource
    perm.action == permission.action
}

# Allow everything for admin as a special case
permission_in_permissions(permission, permissions) {
    perm := permissions[_]
    perm.resource == "*"
    perm.action == "*"
}
