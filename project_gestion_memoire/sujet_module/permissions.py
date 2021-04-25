from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # cette permissionne concerne la modification d'un sujet
        return obj.personnel.user == request.user


# permission pour la modification d'un sujet une fois qu'on veut le terminer
class IsEncadreur(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (request.user.personnel.profil=="ETUDIANT"):
            return False
        # si la personne est  un encadreur d'un sujet, on retourne  True
        if request.user.personnel.id in obj.personnelValider.values_list("id",flat=True):
            return True
        # si la personne est proprietaire du sujet
        return  obj.personnel.user == request.user
