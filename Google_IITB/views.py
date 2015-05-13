from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context 
import datetime
from functions import Search

def django_search(request, search_str):
	query = search_str.replace("+", " ")
	t = get_template('search.html')
	s = Search()
	start = datetime.datetime.now().microsecond
	res = s.searchWSC(query)
	end = datetime.datetime.now().microsecond
	delta = end - start
	if delta < 0: delta = 1000000 + end - start
	if not res['change']:
		c = {'result' : res['search'] ,
			 'query' : query,
			 'original' : query, 
			 'change': False,
			 'number': len(res['search']),
			 'time' : (delta)/1000000.0}
			 
	else: c = {'result' : res['search'], 
			   'query' : res['query'],
			   'original' : query, 
			   'change': True,
			   'number': len(res['search']),
			   'time' : (delta)/1000000.0}
			   
	html = t.render(Context(c))
	return HttpResponse(html)
