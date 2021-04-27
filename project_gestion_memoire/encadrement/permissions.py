from rest_framework import permissions


class IntegrityPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        enseignants = obj.enseignants.values_list("profil",flat=True)
        valide=True
        for profil in enseignants:
            if profil == "ETUDIANT":
                valide = False   
        etudiants = obj.etudiants.values_list("profil",flat=True)
        for profil in etudiants:
            if profil != "ETUDIANT" :
                valide = False
        return  valide
