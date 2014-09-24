from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.template import Template, Context
from eleni_app.models import Project, Photo, Link, About_detail, Contact_info
#from eleni_app.forms import ContactForm
#from django.core.context_processors import csrf
#from django.views.decorators.csrf import csrf_protect
#from django.core.mail import send_mail

#@csrf_protect
def contact(request):
	"""if request.method == 'POST':
		print ("after if request post")
		form = ContactForm(request.POST)
		print (form)
		if form.is_valid():
			print ("we are in form is valid")
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@simplesite.com'),
				['sgkristinsson@gmail.com'], #email address where message is sent.
			)
			if request.is_ajax():
				print ('it was an ajax')
				return render(request, 'thanks.html')
			#print (cd)
			#print (message)
			#print (email)
				print ('does this print')
			#subject = (request.POST.get('subject'))
			else:
				print ("HttpResponseRedirect('/thanks/')")
				return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	print ("origianl request loads contact")
	return render(request, 'contact.html', {'form': form})
	"""
	contact = Contact_info.objects.get(pk=1)
	print (contact.title)
	return render_to_response('contact.html', { 'contact': contact }, context_instance=RequestContext(request))

def enter(request):
	return render(request, 'enter.html')

def home_page(request):
		return render(request, 'base.html')


def eleni(request):
	project = Project.objects.all()
	return render_to_response('eleni.html', { 'projects': project }, context_instance=RequestContext(request))



def about(request):
	about = About_detail.objects.first()



	return render_to_response('about.html', { 'about': about }, context_instance=RequestContext(request))


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


def project_details(request, project_id="1"):
	project_details = Project.objects.get(pk=project_id)
	print (project_details.project_type)
	return render_to_response('project_details.html', { 'project_details': project_details }, context_instance=RequestContext(request))


def thanks(request):
	return render(request, 'thanks.html')

def links(request):
	links = Link.objects.all()

	return render_to_response('links.html', { 'links': links }, context_instance=RequestContext(request))











