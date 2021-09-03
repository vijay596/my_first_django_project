from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def show_page(request):
    dict1 = request.GET
    first_name = dict1['name1']
    last_name = dict1['name2']
    out = {
        "name1": first_name,
        "name2" : last_name
    }

    return render(request, 'index.html',out)