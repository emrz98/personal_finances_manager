from django.shortcuts import render


def main_page(request):
    template = "main-page.html"
    return render(request, template)