from django.core.exceptions import PermissionDenied

class IsAdminMixin: 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.es_administrador:
            raise PermissionDenied
        return super(IsAdminMixin, self).dispatch(request, *args, **kwargs)

def is_admin_required():
    def permisos_requeridos(f):
        def check(request, *args, **kwargs):
            if request.user.is_authenticated and not request.user.es_administrador:
                raise PermissionDenied
            return f(request, *args, **kwargs)
        return check
        
    return permisos_requeridos
