from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Member

def index(request):
    objs = Member.objects.all()
    #template = loader.get_template('index.html')
    context = {
        'members_list': objs,
    }
    return render(request, "index.html", context)
    return HttpResponse(template.render(context, request))
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'detail.html', {'member': member})

def edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.first_name = request.POST['firstname']
    member.middle_name = request.POST['middlename']
    member.last_name = request.POST['lastname']
    member.full_name = request.POST['fullname']
    member.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('members:index'))
    
def post(request):
    return HttpResponse("Posting")