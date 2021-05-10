from django.shortcuts import redirect

def login_required(func):
    def login2(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("user_login")
        return func(request,*args,**kwargs)
    return login2

def admin_only(func):
    def admin2(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("user_login")
        return func(request,*args,**kwargs)
    return admin2