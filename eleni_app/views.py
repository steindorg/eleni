from django.shortcuts import render, render_to_response, RequestContext
from eleni_app.models import Project, Link, About_detail, Contact_info

# The MVC patterns control is presented here.
# View functions deal with database queries
# and which templates to render.

# The enter page function
def enter(request):
	return render(request, 'enter.html')

# The base template
def home_page(request):
		return render(request, 'base.html')

# All Projects are displayed at home view.
def eleni(request):
	project = Project.objects.all()
	return render_to_response('eleni.html', { 'projects': project }, context_instance=RequestContext(request))

def contact(request):
	contact = Contact_info.objects.get(pk=1)
	return render_to_response('contact.html', { 'contact': contact }, context_instance=RequestContext(request))

def about(request):
    about = About_detail.objects.first()
    return render_to_response('about.html', { 'about': about }, context_instance=RequestContext(request))

# View for displaying all projects based on project type
def project(request, pro_name):
	if pro_name == 'theatre':
		project = Project.objects.all().filter(project_type='Theatre').order_by('preview_date').reverse()
		if len(project) == 0:
			project = pro_name

	if pro_name == 'film':
		project = Project.objects.all().filter(project_type='Film').order_by('preview_date').reverse()
		if len(project) == 0:
			project = pro_name

	if pro_name == 'tv':
		project = Project.objects.all().filter(project_type='Tv').order_by('preview_date').reverse()
		if len(project) == 0:
			project = pro_name

	if pro_name == 'various':
		project = Project.objects.all().filter(project_type='Various').order_by('preview_date').reverse()
		if len(project) == 0:
			project = pro_name

	return render_to_response('project.html', { 'project': project}, context_instance=RequestContext(request))

# View for displaying project details
def project_details(request, project_id="1"):
	project_details = Project.objects.get(pk=project_id)
	print (project_details.project_type)
	return render_to_response('project_details.html', { 'project_details': project_details }, context_instance=RequestContext(request))

def links(request):
	links = Link.objects.all()

	return render_to_response('links.html', { 'links': links }, context_instance=RequestContext(request))











