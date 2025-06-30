from rest_access_policy import AccessPolicy

class GeneralAccessPolicy(AccessPolicy):
    """
    statements = [
        {
            "action": ["list","create"], 
            "principal": ["group:COORDINADOR CATASTRAL"],  
            "effect": "allow",
        },
        {
            "action": ["retrieve","update","destroy"], 
            "principal": ["*"],  
            "effect": "allow",
        }
    ]

    def get_policy_statements(self, request, view):
        print(f"User: {request.user}")  # Verifica el usuario
        print(f"Groups: {request.user.groups.all()}")  # Verifica los grupos del usuario
        print(f"Action: {getattr(view, 'action', None)}")
        return super().get_policy_statements(request, view)
        """
    
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["group:COORDINADOR CATASTRAL", "group:RECONOCEDOR PREDIAL"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:COORDINADOR CATASTRAL"],
            "effect": "allow"
        },
        {
            "action": ["update", "destroy"],
            "principal": ["group:COORDINADOR CATASTRAL"],
            "effect": "allow"
        },
        {
            "action": ["*"],
            "principal": ["authenticated"],
            "effect": "deny"
        }
    ]
    