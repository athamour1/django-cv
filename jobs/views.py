from django.shortcuts import render
from django.http import HttpResponse

from .models import Jobpos

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
