from django.shortcuts import render

# Create your views here.
def cover(request):
    return render(request, 'personal_site/cover.html')
