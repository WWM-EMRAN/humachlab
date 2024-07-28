from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello world from index')
    # return render(request, 'index.html')
    return render(request, 'theme1/index.html')
    # return render(request, 'theme2/index.html')
    # return render(request, f'{request.context["theme"]}/index.html')


# def home(request):
#     # return HttpResponse('Hello world from home')
#     # return render(request, 'index.html')
#     return render(request, 'theme1/index.html')
#     # return render(request, 'theme2/index.html')
#     # return render(request, f'{request.context["theme"]}/index.html')


