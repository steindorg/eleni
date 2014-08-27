
		"""if request.is_ajax() and request.method == 'Post':
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
		
		"""
		#if request.method == 'POST':






		model


		"""
    def save(self):
        if not self.photo:
            return            

        super(Photo, self).save()
        photo = Image.open(self.photo_thumbnail)
        #(width, height) = photo.size     
        #size = ( 100, 100)
        #photo = photo.resize(size, Image.ANTIALIAS)
        print(self.photo)
        print(photo)
        photo.save(self.photo.path)
"""  