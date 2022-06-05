from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from diagrams.daigram_form_utils import DiagramFormUtils
from diagrams.diagram_utils import DiagramUtils
from diagrams.forms import ModuleForm, ProcessForm, ProjectForm
from diagrams.models import Module, Process, Project
from users.form_utils import FormUtils


@login_required()
def projects(request):
    """
    :param request:
    :return:
    """
    form = ProjectForm()
    utils = DiagramUtils(request=request)
    instances = utils.get_project_of_user()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form_utils = FormUtils(form, Project, request)
        response = form_utils.save_form_datas()

    context = {
        "instances": instances,
        "form": form,
        "title": "Projects",
        "sub_title": "Projects create and lists here",
        "url": reverse('diagrams:projects')
    }
    return render(request, 'users/project.html', context=context)


@login_required()
def delete_project(request, pk):
    FormUtils.delete_data(pk, Project)
    return redirect(reverse('diagrams:projects'), )


@login_required()
def modules(request, pk):
    """
    :param request:
    :return:
    """
    form = ModuleForm()
    instances = DiagramUtils.get_all_modules(pk)
    project_instance = DiagramUtils.get_project_instance_by_id(pk)

    if request.method == 'POST':
        form = ModuleForm(request.POST)
        form_utils = DiagramFormUtils(form, Module, request)
        response = form_utils.save_module_datas(project_instance)
        print(response)

    context = {
        "instances": instances,
        "form": form,
        "title": "Modules",
        "sub_title": f"Modules created for project {project_instance.name}",
        "url": reverse('diagrams:modules', kwargs={'pk': pk}),
    }
    return render(request, 'users/module.html', context=context)


@login_required()
def delete_module(request, pk):
    instance = Module.objects.get(pk=pk)
    FormUtils.delete_data(pk, Module)
    return redirect(reverse('diagrams:modules', kwargs={'pk': instance.project.pk}), )


@login_required()
def process(request, pk):
    """
    :param pk:
    :param request:
    :return:
    """
    form = ProcessForm()
    print("Id tis ", pk)
    instances = DiagramUtils.get_all_modules_of_process(pk)
    module_instance = DiagramUtils.get_module_instance_by_id(pk)

    if request.method == 'POST':
        form = ProcessForm(request.POST)
        form_utils = DiagramFormUtils(form, Process, request)
        response = form_utils.save_process_datas(module_instance)
        print("response is ", response)
        return redirect(reverse('diagrams:process', kwargs={'pk': pk}))

    context = {
        "instances": instances,
        "form": form,
        "title": "Process",
        "sub_title": f"Process for the module {module_instance.name}",
        "url": reverse('diagrams:process', kwargs={'pk': pk}),
    }
    return render(request, 'users/process.html', context=context)


@login_required()
def delete_process(request, pk):
    instance = Process.objects.get(pk=pk)
    FormUtils.delete_data(pk, Process)
    return redirect(reverse('diagrams:process', kwargs={'pk': instance.module.pk}), )
