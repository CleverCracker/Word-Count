from django.http import HttpResponse
from django.shortcuts import render
import operator


def Home(request):
    return render(request, 'home.html', {'name': "Gulfam"})


def Count(request):
    fulltxt = request.GET['fulltext']
    print(fulltxt)
    wordList = fulltxt.split()
    dictonary = {}
    for word in wordList:
        if word in dictonary:
            dictonary[word] += 1
        else:
            dictonary[word] = 1
    data = {
        'fulltext': fulltxt,
        'count': len(wordList),
        'dictonary': sorted(dictonary.items(), key=operator.itemgetter(1), reverse=True)
    }
    return render(request, 'count.html', data)


def About(request):
    return render(request, 'about.html')
