from django.conf.urls import patterns, include, url

urlpatterns = patterns('game.views',
        url(r'^word-turn-over/$', 'wordtutor', name='wordtutor'),
        url(r'^word-turn-over/add/$', 'wordtutor_add', name='wordtutor_add'),
        url(r'^word-turn-over/set/$', 'wordtutor_set', name='wordtutor_set'),
        url(r'^word-turn-over/get/$', 'wordtutor_get', name='wordtutor_get'),
        url(r'^word-turn-over/record/$', 'wordtutor_record', name='wordtutor_record'),
)
