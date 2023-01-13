from django.shortcuts import render, HttpResponse, redirect
from project.models import MyProject
from project.templatetags import extras


# Create your views here.
def projecthome(request):
    allpost = MyProject.objects.all()
    context = {'allpost' : allpost}
    return render(request, 'project/projecthome.html', context)


def projectpost(request, slug):
    project = MyProject.objects.filter(slug=slug).first()
    project.views = project.views + 1
    project.save()
    allpost = MyProject.objects.all()
    context = {'project' : project, 'allpost' : allpost}
    return render(request, 'project/projectpost.html', context)

# def projectcomments(request):
#     return render(request, 'project/projecthome.html')
