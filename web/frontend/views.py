"""
URLs for the Kando frontend. Should exist at the domain root.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Task


@login_required(login_url='/admin/login/')
def index(request):
    """
    The root view for the Kando frontend.
    """
    user = request.user
    to_dos = Task.objects.to_do().filter(assignee=user)
    reviews = Task.objects.review().filter(reviewer=user)

    return render(
        request,
        'frontend/index.html',
        {
            'review_list': reviews,
            'to_do_list': to_dos
        })


@login_required(login_url='/admin/login/')
def doing(request):
    """
    Doing view for the Kando frontend.
    """
    user = request.user
    doing = Task.objects.doing().filter(assignee=user)
    recently_completed = Task.objects.done().filter(assignee=user)

    return render(
        request,
        'frontend/index.html',
        {
            'doing_list': doing,
            'done_list': recently_completed
        })


@login_required(login_url='/admin/login/')
def review(request):
    """
    Review view for the Kando frontend.
    """
    user = request.user
    reviews = Task.objects.review().filter(reviewer=user)

    return render(
        request,
        'frontend/index.html',
        {
            'review_list': reviews
        })


@login_required(login_url='/admin/login/')
def done(request):
    """
    Done view for the Kando frontend.
    """
    user = request.user
    done = Task.objects.doing().filter(assignee=user)

    return render(
        request,
        'frontend/index.html',
        {
            'done_list': done
        })
