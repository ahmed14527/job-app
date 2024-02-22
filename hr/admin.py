from django.contrib import admin
from .models import Hr, JobPost, CandidateApplications, SelectCandidateJob

admin.site.register(Hr)
admin.site.register(JobPost)
admin.site.register(CandidateApplications)
admin.site.register(SelectCandidateJob)