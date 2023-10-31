from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import UrlForm
from django.views.generic import TemplateView
from .shorten import Shortener

def redirect_to_original_url(request, token):
    long_url = ShortenedURL.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def shorten_url(request):
    form = UrlForm(request.POST)
    token = ""
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            token = Shortener().generate_token()
            new_url.short_url = token
            new_url.save()
    else:
        form = UrlForm()
        token = "Invalid URL"

    return render(request, 'home.html', {'form': form, 'token': token})
def url_list(request):
    url_entries = ShortenedURL.objects.all()
    context = {'url_entries': url_entries}
    return render(request, 'url_list.html', context)