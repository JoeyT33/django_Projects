from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'survey.html')

def submitSurvey(request):
    print(request.POST["fname"])
    context = {
        'surveyinfo': request.POST
    }
    return render(request, 'submit.html', context)
