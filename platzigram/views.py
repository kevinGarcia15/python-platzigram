#Django
from django.http import HttpResponse
#utilities
from datetime import datetime
#django
from django.http import JsonResponse
import json
def hellow_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(
        'hellow world current server time is {now}'.format(now=now)
        )
def sort_integers(request):
#    import pdb; pdb.set_trace()  para hacer debuggin
    # numbers = map(lambda x : int(x),request.GET["number"].split(","))
    # return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})
    numbers = [int(i) for i in request.GET['number'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
    'status': 'ok',
    'numbers': sorted_ints,
    'message': 'integer sorted successfully'
    }
    #es una forma de enviar json como una API
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def home(reqiest, name, age):
    if age <= 12:
        message = 'Sorry {}, you are ot allowed here'.format(name)
    else:
        message = 'Hello, {}! Welocome to platzigram'.format(name)
    return HttpResponse(message)
