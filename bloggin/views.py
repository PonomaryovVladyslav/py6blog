from django.http import HttpResponse


def username(request):
    return HttpResponse("here will be username")


def blogs(request):
    return HttpResponse("here will be blogs")


def about(request):
    return HttpResponse("here will be about")


def oneblog(request, txt):
    return HttpResponse(f"here will be oneblog, address {txt}")


def comment(request, txt):
    return HttpResponse(f"here will be comment, address {txt}")


def create(request):
    return HttpResponse("here will be create")


def update(request, txt):
    return HttpResponse(f"here will be update, address {txt}")


def delete(request,txt):
    return HttpResponse(f"here will be delete, address {txt}")

