from django.shortcuts import redirect


def redirect_to_main(request):
    return redirect("index")
