from django.shortcuts import render
from student import models
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
# Create your views here.

# def index(request):
#     students=models.Student.objects.all()
#     if request.method=='POST':
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             cleaned_data=form.cleaned_data
#             student=models.Student()
#             student.name=cleaned_data['name']
#             student.sex=cleaned_data['sex']
#             student.email=cleaned_data['email']
#             student.phone=cleaned_data['phone']
#             student.profession=cleaned_data['profession']
#             student.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form=StudentForm()
#
#     context={'students':students,'form':form}
#     return render(request,'index.html',context=context)

# def index(request):
#     students=models.Student.get_all()
#     if request.method=='POST':
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form=StudentForm()
#
#     context={'students':students,'form':form}
#     return render(request,'index.html',context=context)

class IndexView(View):
    template_name='index.html'

    def get_context(self):
        students=models.Student.get_all()
        context={'students':students}
        return context

    def get(self,request):
        context=self.get_context()
        form=StudentForm()
        context.update({'form':form})
        return render(request,self.template_name,context=context)

    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
            # context=self.get_context()
            # context.update({'form':form})
            # return render(request,self.template_name,context) # 可以模仿异步 
        else:
            context=self.get_context()
            context.update({'form':form})
            return render(request,self.template_name,context=context)


