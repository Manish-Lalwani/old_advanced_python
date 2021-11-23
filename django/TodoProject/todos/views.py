from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_todo_items(request):
    #return HttpResponse("Views: list_todo_items called")
    return render(request,'todos/todos_list.html')