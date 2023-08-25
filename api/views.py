from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Course
from django.views.decorators.csrf import csrf_exempt
import json
def index(request):
    return HttpResponse("Hello")

def loadData(request):
    f = open('courses.json')
    courses = json.load(f)
    for course in courses:
        new_course = Course(title=course['title'],author=course['author'],overview=course['overview'],image=course['img'],url=course['url'])
        new_course.save()
    f.close()
    return HttpResponse('Data loaded successfully')

def listData(request):
    course = Course.objects.all()
    return render(request, 'courses_view.html', {'course' : course})

@csrf_exempt
def deleteCourse(request, course_id):
  Item = Course.objects.get(id = course_id)
  Item.delete()
  return HttpResponseRedirect('/')

@csrf_exempt
def searchCourse(request):
    content = request.POST['query']
    items = Course.objects.filter(title__icontains=content)
    return render(request, 'courses_view.html', {'course' : items})
