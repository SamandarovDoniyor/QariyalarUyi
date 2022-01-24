from django.db import models
from django.shortcuts import redirect, render
from backend import models

def About(request):
    template_name = "About.html"
    organ = models.Organizers.objects.all()
    context = {
        'organ':organ
    }
    return render(request,template_name,context)


def Home(request):
    template_name = 'index.html'
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        if name and comment:
            models.Comment.objects.create(comment_name=name,
                                          comment=comment)

    new = models.News.objects.all()
    comments = models.Comment.objects.all()
    context = {
        'new': new,
        'comments': comments
    }

    return render(request, template_name, context)




def Partners(request):
    template_name = 'Partners.html'
    part = models.Partners.objects.all()
    context = {
        "part":part
    }
    return render(request,template_name,context)

def News(request):
    new = models.News.objects.all()
    context = {
        'new':new
    }
    template_name = 'news.html'
    return render(request,template_name,context)

def Charities(request):
    donat = models.Donat.objects.all()
    context = {
        'donat':donat
    }
    template_name = 'Charities.html'
    return render(request,template_name,context)

def Elderly(request):
    elderlys = models.Elderly.objects.all() 
    template_name = 'Elderly.html'
    context = {
        'elderlys':elderlys
    }
    
    return render(request,template_name,context)



def Archive(request):
    template_name = "Archive.html"
    archives = models.Archive.objects.all()
    context = {
        'archives':archives
    }
    return render(request,template_name,context)


def VideoGalary(request):
    template_name = "Videogallery.html"
    videoGy = models.VideoGalary.objects.all()
    context = {
        'videoGy':videoGy
    }
    return render(request,template_name,context)
    
    
def PhotoGalary(request):
    photo = models.PhotoGalary.objects.all()
    template_name = "Photogallery.html"
    context = {
        'photo':photo
        
    }
    return render(request,template_name,context)




# def post(reuqest):
#     forms = 




        