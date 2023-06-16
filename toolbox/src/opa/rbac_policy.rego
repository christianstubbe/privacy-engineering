package accesscontrol

# Define roles and their permissions
roles = {
    "admin": ["create", "read", "update", "delete"],
    "editor": ["read", "update"],
    "viewer": ["read"]
}

# Check if a user has permission to perform an action
allow {
    # Retrieve the user's role from the input
    user_role := input.user.role
    
    # Retrieve the action from the input
    action := input.action

    # Check if the action is in the role's permissions
    roles[user_role][_] == action
}
