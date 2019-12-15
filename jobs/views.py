from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Jobpos, Candidates
from .forms import CandidatesForm

def index(request):
    jobs = Jobpos.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(request, "jobs.html", context)
    # return HttpResponse(jobs[0].title)

def job(request, job_id):
    try:
        job = Jobpos.objects.get(pk=job_id)
    except Question.DoesNotExist:
        raise Http404("job does not exist")
    return render(request, 'job.html', {'job': job})


def form(request, job_id):
    if request.method == 'POST':
        form = CandidatesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fullname = data['fullname']
            email = data['email']
            phone = data['phone']
            interested = data['interested']
            github = data['github']
            article = data['article']
            Candidates.objects.create(fullname=fullname, email=email, phone=phone, interested=interested, github=github, article=article, job_id=job_id)
            return HttpResponseRedirect('/jobs/')
    else:
        form = CandidatesForm()
    return render(request, 'form.html', {'id':job_id, 'form':form})
