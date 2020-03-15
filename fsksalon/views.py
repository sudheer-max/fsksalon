from django.shortcuts import render
from .models import AboutUs, Hair, Portfolio, Blog, Course, Beauty, Bridal, Tattoo, Nail
from django.views.generic import ListView, DetailView

def beauty(request):
    context = {
        'beautys' : Beauty.objects.all()
    }
    template = "beauty.html"
    return render(request, template, context)

class beautyView(ListView):
    model = Beauty
    template_name = "beauty.html"

class beautyDetailView(DetailView):
    model = Beauty
    template_name = "beauty-detail.html"

def course(request):
    context = {
        'courses' : Course.objects.all()
    }
    template = "course.html"
    return render(request, template, context)

class courseView(ListView):
    model = Course
    template_name = "course.html"

class courseDetailView(DetailView):
    model = Course
    template_name = "course-detail.html"

def blog(request):
    context = {
        'blogs' : Blog.objects.all()
    }
    template = "blog.html"
    return render(request, template, context)

class blogView(ListView):
    model = Blog
    template_name = "blog.html"

class blogDetailView(DetailView):
    model = Blog
    template_name = "blog-detail.html"

def portfolio(request):
    context = {
        'portfolios' : Portfolio.objects.all()
    }
    template = "portfolio.html"
    return render(request, template, context)

class portfolioView(ListView):
    model = Portfolio
    template_name = "portfolio.html"

def bridal(request):
    context = {
        'bridals' : Bridal.objects.all()
    }
    template = "bridal.html"
    return render(request, template, context)

class bridalView(ListView):
    model = Bridal
    template_name = "bridal.html"

def tattoo(request):
    context = {
        'tattoos' : Tattoo.objects.all()
    }
    template = "tattoo.html"
    return render(request, template, context)

class tattooView(ListView):
    model = Tattoo
    template_name = "tattoo.html"

def nail(request):
    context = {
        'nails' : Nail.objects.all()
    }
    template = "nail.html"
    return render(request, template, context)

class nailView(ListView):
    model = Nail
    template_name = "nail.html"

def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)


def about(request):
    return render(request, "about.html")





def hair(request):
    context = {
        'hairs' : Hair.objects.all()
    }
    template = 'hair.html'
    return render(request, template, context)

class HairView(ListView):
    model = Hair
    template_name = 'hair.html'


class HairDetailView(DetailView):
    model = Hair
    template_name = 'hair-detail.html'


