from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее только администратору редактировать его.
    """

    def has_permission(self, request, view):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff