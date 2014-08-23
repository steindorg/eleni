from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

# Create your views here.


def contact(request):
		if request.is_ajax() and request.method == 'Post':
				form = ContactForm(request.POST)
				if form.is_valid():
					cd = form.cleaned_data
					send_mail(
						cd['subject'],
						cd['message'],
						cd.get('email', 'noreply@simplesite.com'),
						['sgkristinsson@gmail.com'], #email address where message is sent.
					)
					return HttpResponseRedirect('/thanks/')
				else:
					return HttpResponse('your ajax test did not work')
		else:
			form = ContactForm()
		return render(request, 'contact.html', {'form': form})

def thanks(request):
	return render(request, 'thanks.html')
