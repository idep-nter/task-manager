from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, FormView,UpdateView, DeleteView
from django.utils.decorators import method_decorator

from .models import Task, User
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = "manager/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context["users"] = users
        return context


@method_decorator(login_required, name='dispatch')
class TasksView(ListView):
    template_name = "manager/tasks.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(owner=self.request.user).order_by('complete',
                                                                   'date_added')
        return data


@method_decorator(login_required, name='dispatch')
class NewTaskView(FormView):
    form_class = TaskForm
    template_name = "manager/new_task.html"
    success_url = "/tasks"

    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.owner = self.request.user
        new_task.save()
        return super().form_valid(new_task)


@method_decorator(login_required, name='dispatch')
class UpdateTaskView(UpdateView):
    template_name = "manager/update_task.html"
    model = Task
    fields = ["title", "description", "complete"]
    success_url = "/tasks"


@method_decorator(login_required, name='dispatch')
class DeleteTaskView(DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "manager/delete_task.html"
    success_url = "/tasks"