from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import ConfessionForm
from.models import Confession
from django.contrib import messages

# Create your views here.


class Home(View):
    def get(self,request):
        confessions = Confession.objects.filter(is_approved = True).order_by("-created_at")
        return render(request,"home.html",{"confessions":confessions})
    



class SubmitConfession(View):
    def get(self,request):
        form = ConfessionForm()
        return render(request,"submit.html",{"form":form})


    def post(self,request):
        form = ConfessionForm(request.POST)
        if form.is_valid():
            confession = form.save(commit=False)
            confession.is_approved = False
            confession.save()
            messages.success(
                request,
                "Your confession has been submitted and is waiting for approval. It may take some time"
            )
            return redirect("home")
        
        return render(request,"submit.html",{"form":form})




class ConfessionDetail(View):
    def get(self,request,pk):
        confession = get_object_or_404(Confession,pk=pk,is_approved=True)
        return render(request,'confession_detail.html',{"confession":confession})