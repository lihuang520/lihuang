from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from package import get_baidu
# Create your views here.
def index(request):
	#return HttpResponse('lihuang')
	return render(request,'index.html')



def so(request):
	wd = request.GET.get('wd',None)
	if not wd:
		return HttpResponseRedirect('/')
	html = get_baidu.get_info(wd)
	return HttpResponse('lihuang')