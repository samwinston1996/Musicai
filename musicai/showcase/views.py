from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Gallery

@login_required
def showcase(request):
    data = {
        "gallery": Gallery.objects.filter(visible=True).order_by("-date_created")
    }
    return render(request, "showcase/showcase.html", data)