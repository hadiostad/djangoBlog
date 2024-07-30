from django.shortcuts import render



def main_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    pass


def single_post(request):
    pass
