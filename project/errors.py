from django.shortcuts import redirect


def error_badrequest(request, exception=None):
    # 400
    return redirect("home")


def error_forbidden(request, exception=None):
    # 403
    return redirect("home")


def error_notfound(request, exception=None):
    # 404
    return redirect("home")


def error_servererror(request):
    # 500
    return redirect("home")
