from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):

    return render(request,'testapp/index.html')

def result_view(request):
    name_data = request.GET.get('fullname', 'default')
    textarea_data = request.GET.get('textarea', 'default')
    checkbox_capital = request.GET.get('capital','off')
    checkbox_special = request.GET.get('special_char','off')
    checkbox_number = request.GET.get('number','off')
    fullname = str(name_data).split(' ')

    text_data = str(textarea_data)
    #logic for capiatalize
    if checkbox_capital == 'on':
        text_data = text_data.upper()
    #logic for Removing Special Charecter
    if checkbox_special == 'on':
        analyzed = ''
        for i in text_data:
            if i.isalnum():
                analyzed = analyzed + i
        text_data = analyzed
    #logic for Removing Numbers
    if checkbox_number == 'on':
        analyzed = ''
        for i in text_data:
            if not i.isnumeric():
                analyzed = analyzed + i
        text_data = analyzed
    #if Nothing Selected
    elif checkbox_capital == 'off' and checkbox_number == 'off' and checkbox_special == 'off':
        return HttpResponse('<H2>PLESE CLICK ON atleast one CHECKBOX !!</H2> <a href="/home"><button type="button" class="btn btn-dark">BACK</button></a>')
    #final o/p
    return render(request, 'testapp/result.html', {'fullname': fullname[0], 'analyzed': text_data})


def about_view(request):
    return render(request, 'testapp/about.html')

def contact_view(request):
    return render(request, 'testapp/contact.html')
