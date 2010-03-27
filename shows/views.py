from django.views.generic.simple import direct_to_template

from tvdb_api import Tvdb
from tvdb_exceptions import tvdb_error, tvdb_shownotfound

from shows.forms import ShowSearchForm, ShowForm

def add(request):
    if request.method == 'POST':
        search_form = ShowSearchForm(request.POST)
        if search_form.is_valid():
            show_query = search_form.cleaned_data['show']
            tv = Tvdb()
            try:
                show = tv[show_query]
            except tvdb_shownotfound, e:
                search_form = e.message
                error_msg = e.message # TODO: use errorlist instead?
            except tvdb_error, e:
                error_msg = e.message
            else:
                show_data = {
                    'name': show.data['seriesname'],
                    'description': show.data['overview'],
                    'actors': show.data['actors'],
                    'genre': show.data['genre'],
                    'status': show.data['status'],
                    'imdb_id': show.data['imdb_id'],
                    'zap2it_id': show.data['zap2it_id']
                }
                show_form = ShowForm(show_data)
                if show_form.is_valid():
                    new_show = show_form.save()
    else:
        search_form = ShowSearchForm()
    return direct_to_template(request, 'shows/add.html', locals())

def delete(request):
    pass

def info(request):
    pass

def update(request):
    pass