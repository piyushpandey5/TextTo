from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('''this is about page  about''')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # print(removepunc)
    if(removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctutaions','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'in uppercase','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if(char!='\n' and char!='\r'):
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed NewLines','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for char in djtext:
            if(char!='  '):
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('Error')

# def capfirst(request):
#     return HttpResponse("capfirst page page")

# def newlineremove(request):
#     return HttpResponse("new line remover page")

# def spaceremove(request):
#     return HttpResponse("spaceremove page")

# def charcount(request):
#     return HttpResponse("charcount")