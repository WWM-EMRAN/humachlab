from django import forms
from django.contrib import admin
from .models import KeyInformation, SkillsAndTools, HonorsAndAwards, CertificationsCoursesTrainings, Projects, Memberships, SessionsOrEvents, Languages, Portfolios, Volunteering, Publications, Contacts
from .widgets import MultipleFileInput  # Import the custom widget


# Register your models here.
admin.site.register(KeyInformation)
admin.site.register(SkillsAndTools)
admin.site.register(HonorsAndAwards)
admin.site.register(CertificationsCoursesTrainings)
admin.site.register(Projects)
admin.site.register(Memberships)
admin.site.register(SessionsOrEvents)
admin.site.register(Languages)
admin.site.register(Portfolios)
admin.site.register(Volunteering)
admin.site.register(Publications)
admin.site.register(Contacts)




# ### Customising Project form for image upload
# class ProjectsAdminForm(forms.ModelForm):
#     # images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
#     images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)
#
#     class Meta:
#         model = Projects
#         # fields = ['project_position', 'project_title', 'project_description', 'project_fund',
#         #           'project_funding_organisation', 'project_collaboration_organisation', 'project_start_date',
#         #           'project_end_date', 'project_images']
#         fields = ['project_position', 'project_title', 'project_description', 'project_fund',
#                   'project_funding_organisation', 'project_collaboration_organisation', 'project_start_date',
#                   'project_end_date']
#
# class ProjectsAdmin(admin.ModelAdmin):
#     form = ProjectsAdminForm
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.enctype = 'multipart/form-data'
#         form.method = 'POST'
#         return form
#
#     def save_model(self, request, obj, form, change):
#         """Override to save one or more images."""
#         obj.save()  # Save the object to generate the primary key (if new)
#         # images = form.cleaned_data.get('images')
#         images = request.FILES.getlist('images')  # Fetch images from the request
#         if images:
#             obj.save_images(images)  # Save the images and update the database
#
# admin.site.register(Projects, ProjectsAdmin)




