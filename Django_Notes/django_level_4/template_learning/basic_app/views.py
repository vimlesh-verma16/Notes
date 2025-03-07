from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "basic_app/index.html", {"vimlesh": "I am vimlesh"})


def other(request):
    return render(request, "basic_app/other.html")


def relative(request):
    return render(request, "basic_app/relative_urls_template.html")
