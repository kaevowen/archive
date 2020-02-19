from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(req):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(req, 'shareRes/index.html', content)


def restaurantDetail(req):
    return render(req, 'shareRes/restaurantDetail.html')


def restaurantCreate(req):
    return render(req, 'shareRes/restaurantCreate.html')


def categoryCreate(req):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(req, 'shareRes/categoryCreate.html', content)


def Create_category(req):
    category_name = req.POST['categoryName']
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('shareRes'))


def Delete_category(req):
    print("req : ", req.POST.keys())
    category_id = req.POST['categoryId']
    print(category_id)
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))