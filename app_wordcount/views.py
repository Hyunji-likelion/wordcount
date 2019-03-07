from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request, 'home.html')

def about(request) :
    return render(request, 'about.html')

def result(request) :
    text = request.GET['fulltext']
    textlist = text.split()
    # 총 단어수는 = len(textlist)
    text_dictionary = {}
    for word in textlist :
        if word in text_dictionary :
            text_dictionary[word]+=1
        else :
            text_dictionary[word]=1   

    return render(request, 'result.html', {'full': text, 'total' : len(textlist),'dictionary' : text_dictionary.items() })