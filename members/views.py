from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import View
from .models import Member
from .forms import MyForm

class IndexView(View):

    def get(self, request):
        objs = Member.objects.all()
        context = {
            'members_list': objs,
        }
        return render(request, "index.html", context)

class DetailView(View):

    def get(self, request, member_id):
        member = get_object_or_404(Member, pk=member_id)
        context = {
            'member': member,
        }
        return render(request, 'detail.html', context)

class EditView(View):

    def get(self, request, member_id):
        member = get_object_or_404(Member, pk=member_id)
        context = {
            'member': member,
        }
        return render(request, 'edit.html', context)

    def post(self, request, member_id):
        form = MyForm(request.POST)
        member = get_object_or_404(Member, pk=member_id)

        if form.is_valid():
            member.first_name = form.cleaned_data['first_name']
            member.middle_name = form.cleaned_data['middle_name']
            member.last_name = form.cleaned_data['last_name']
            member.full_name = form.cleaned_data['full_name']
            member.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse("members:index"))
        else:
            context = {
                'error_message': 'Form invalid.',
                'member': member,
            }
            return render(request, 'edit.html', context)
        