from django.shortcuts import render
from django.shortcuts import redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create_news.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    context_object_name = 'article'
    template_name = 'news/news_delete.html'



def create_news(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Form invalid"
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create_news.html', data)
