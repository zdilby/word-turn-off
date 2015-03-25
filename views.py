from django.shortcuts import render,render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.template import RequestContext, Context, Template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _, ugettext
from django.db.models import Count
from utils.json_utils import JsonHttpResponse 

from game.models import Words,WordsSet

# Create your views here.
def update(p):
    setting = WordsSet.objects.get(pk=1)
    if not p['page'] or not p['page'].isdigit():
        p['page'] = 1
    else:
        p['page'] = int(p['page'])
    p['num'] = setting.pernum
    if p['length']:
        p['page'] = (p['page']-1)%((p['length']+p['num']-1)/p['num'])+1
    p['start'],p['end'] = (p['page']-1)*p['num'],p['page']*p['num']
    if setting.orderby == 'alpha':
        p['orderby'] = 'title'
    p['show_orderby'] = _(setting.orderby)
    return p

def wordtutor(request):
    setting = WordsSet.objects.get(pk=1)
    context = {}
    if not setting.cur_cla:
        setting.cur_cla = 'TOEFL'
    if not setting.orderby:
        setting.orderby= 'title'

    context['classify'] = setting.cur_cla
    results = Words.objects.filter(classify=setting.cur_cla).order_by(setting.orderby)
    if results:
        results = results[:setting.pernum]

    context['hide'] = request.GET.get('hide','')
    context['p'] = {'num':setting.pernum,'show_orderby':_(setting.orderby)} 
    context['results'] = results
    context['classes'] = [ i['classify'] for i in Words.objects.all().values('classify').annotate(dcount=Count('classify'))]
    return render_to_response('game/wordtutor.html', context, context_instance=RequestContext(request))

def wordtutor_get(request):
    context,p = {},{}
    for i in ['classify','page']:
        p[i] = request.GET.get(i,'')

    setting = WordsSet.objects.get(pk=1)
    if p['classify']:
        setting.cur_cla= p['classify']   
        setting.save()
        results = Words.objects.filter(classify=p['classify']).order_by(setting.orderby)
    elif setting.cur_cla:
        results = Words.objects.filter(classify=setting.cur_cla).order_by(setting.orderby)
    else:
        results = Words.objects.filter(classify='TOEFL').order_by(setting.orderby)

    p['length'] = results.count()
    p = update(p)
    context['p'] = p

    if results:
        results = results[p['start']:p['end']]
    results = [{'level':i.level,'classify':i.classify,'title':i.title,'features':i.features} for i in results]
    context['results'] = results
    return JsonHttpResponse(context)

def wordtutor_add(request):
    p = {}
    result = {}
    for i in ['word','features','classify']:
        p[i] = request.GET.get(i, '')
        if not p[i]:
            result['status'] = "Failed"
            result['error'] = i
            return JsonHttpResponse(result)

    try:
        word,created = Words.objects.get_or_create(           
                classify = p['classify'],
                title = p['word']   
            )
        word.level = 1
        word.features = p['features']
        word.save()
    except:
        result['status'] = "Failed"     
        result['error'] = 'create wrong'     
        return JsonHttpResponse(result)
    result = p
    result['status'] = "OK"
    return JsonHttpResponse(result)

def wordtutor_set(request):
    p = {}
    result = {}
    for i in ['orderby','pernum']:
        p[i] = request.GET.get(i, '')
        if not p[i]:
            result['status'] = "Failed"
            result['error'] = i
            return JsonHttpResponse(result)
        if i in ['pernum'] and not p[i].isdigit():
            result['status'] = "Failed"
            result['error'] = i
            return JsonHttpResponse(result)
    try:
        setting,created = WordsSet.objects.get_or_create(pk = 1)
        setting.orderby = '?' if p['orderby'] == 'random' else 'title'
        setting.pernum = p['pernum']   
        setting.save()
    except:
        result['status'] = "Failed"     
        result['error'] = 'create wrong'     
        return JsonHttpResponse(result)
    result = p
    result['status'] = "OK"
    return JsonHttpResponse(result)

def wordtutor_record(request):
    result = [ {'classify':i['classify'],'num':i['dcount']} for i in Words.objects.all().values('classify').annotate(dcount=Count('classify'))]
    return JsonHttpResponse(result)

