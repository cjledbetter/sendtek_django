from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("<h1>This is the Music app homepage!</h1>")


def time1(request):
    now = datetime.datetime.now()
    html = "<html><h1>This is a Music app timepage!</h1><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
