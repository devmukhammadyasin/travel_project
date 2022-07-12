from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Category, Direction,Message, News, Subscribe
from django.contrib import messages

# Create your views here.

class HomePageView(View):
    def get(self, request):
        directions = Direction.objects.all()
        context = {'directions':directions}
        return render(request, "index.html", context)

    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        Subscribe.objects.create(name=name, email=email)
        messages.add_message(request, messages.SUCCESS, "Obunangiz tasdiqladi !")


def change_lang(request):
    lang = request.GET.get('current_lang')
    if lang in ['uz','ru','en']:
        request.session['lang'] = lang
    return JsonResponse({"status":200})

class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')    

class NewsView(View):
    def get(self,request):
        n = News.objects.all()
        c = Category.objects.all()
        context = {
            'all_news':n,
            'category':c,
        }
        return render(request, 'news.html', context)

class ContactView(View):
    def get(self,request):
        return render(request, 'contact.html') 

    def post(self,request):
        print()
        print()
        print(request.POST.get('name'))
        print()
        print()

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']  
        Message.objects.create(name=name, email=email, subject=subject, message=message)
        messages.add_message(request, messages.SUCCESS, "Xabaringiz qabul qilindi !")
        return render(request=request, template_name="contact.html") 