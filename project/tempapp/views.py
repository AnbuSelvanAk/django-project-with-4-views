from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	s='<html><body bgcolor="blue"><h1><font color="white">hello</font></h1></body></html>'
	return HttpResponse(s)
def myfunction1(request):
	a='<html><body bgcolor="blue"><h1><font color="white">hii</font></h1></body></html>'
	return HttpResponse(a)
def myfunction2(request):
	b='<html><body bgcolor="blue"><h1><font color="white">anbu</font></h1></body></html>'
	return HttpResponse(b)
def myfunction3(request):
	c='<html><body bgcolor="blue"><h1><font color="white">abc</font></h1></body></html>'
	HttpResponse(c)
	