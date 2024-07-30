from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse("hii")


def posts(request):
    pass


def single_post(request):
    pass
