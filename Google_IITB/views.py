from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context 
import datetime
from functions import Search


def django_search(request):
	query = request.GET.get('q', '')
	t = get_template('search.html')
	s = Search()
	start = datetime.datetime.now().microsecond
	res = s.searchWSC(query)
	end = datetime.datetime.now().microsecond
	delta = end - start
	if delta < 0: delta = 1000000 + end - start
	if not res['change']:
		c = {'result' : res['search'],
			 'query' : query,
			 'original' : query,
			 'spaced_query' : query,
			 'change': False,
			 'number': len(res['search']),
			 'time' : (delta)/1000000.0}
			 
	else: c = {'result' : res['search'], 
			   'query' : res['query'],
			   'original' : query,
			   'spaced_query' : res['query'].replace('+',' '),
			   'change': True,
			   'number': len(res['search']),
			   'time' : (delta)/1000000.0}
			   
	html = t.render(Context(c))
	return HttpResponse(html)
	

