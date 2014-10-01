from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from eleni_app.models import Project, Video_Link, Photo, Link, About_detail, Contact_info

# Models that are manageble in the django admin interface

class ProjectAdmin(admin.ModelAdmin):
	# What is displayed in the admin edit view
	list_display = ('title', 'project_type')
	# Makes all photos chooseable in a horizontal display
	filter_horizontal = ('photos',)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', 'image_img')


class Video_LinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'title')

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'title')


class About_detailAdmin(admin.ModelAdmin):
	list_display = ('title', 'title')

class Contact_infoAdmin(admin.ModelAdmin):
	list_display = ('title', 'title')

# Registering models
admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video_Link, Video_LinkAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(About_detail, About_detailAdmin)
admin.site.register(Contact_info, Contact_infoAdmin)


