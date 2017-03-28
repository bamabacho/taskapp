from django.shortcuts import render
from django.utils import timezone
from .models import Task, Board
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def board_list(request):
	boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'tasks/board_list.html', {"boards":boards})

def task_list(request):
	tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'tasks/task_list.html', {'tasks':tasks})

def post_detail(request, pk):
	task = get_object_or_404(Task, pk=pk)
	return render(request, 'tasks/task_detail.html', {'task':task} )

def post_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = PostForm(instance=task)
    return render(request, 'tasks/post_edit.html', {'form': form})




	


def post_new(request):

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.created_date = timezone.now()
			task.save()
			return redirect('task_list')
	else:
		form=PostForm()
	return render(request, 'tasks/post_edit.html', {'form':form})

