from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import ConfessionForm,CommentForm
from.models import Confession,Comment
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
        comments = confession.comments.all().order_by("-created_at")
        form = CommentForm()
        return render(request,'confession_detail.html',{
            "confession":confession,
            "comments":comments,
            "form":form
        })
    
    def post(self,request,pk):
        confession = get_object_or_404(Confession,pk=pk,is_approved=True)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.confession = confession
            comment.save()

        return redirect("confession-detail",pk=pk)
