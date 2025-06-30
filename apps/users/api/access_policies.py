from rest_access_policy import AccessPolicy

class UserAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ["group:COORDINADOR", "group:RECONOCEDOR PREDIAL"],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:COORDINADOR"],
            "effect": "allow"
        },
        {
            "action": ["update", "destroy"],
            "principal": ["group:COORDINADOR"],
            "effect": "allow"
        },
        {
            "action": ["*"],
            "principal": ["authenticated"],
            "effect": "deny"
        }
    ]
