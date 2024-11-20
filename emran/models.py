import os
from pathlib import Path
import json
from django.db import models
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField



# Create your models here.


## KeyInformation model
class KeyInformation(models.Model):
    ki_type = models.CharField(max_length=300)
    ki_amount = models.IntegerField()
    ki_names = models.CharField(max_length=500)
    ki_sort_description = models.TextField(null=True, blank=True)


## SkillsAndTools model
class SkillsAndTools(models.Model):
    sat_title = models.CharField(max_length=300)
    sat_short_description = models.CharField(max_length=600)
    sat_description = models.TextField(null=True, blank=True)
    sat_skill_level = models.IntegerField()


## HonorsAndAwards model
class HonorsAndAwards(models.Model):
    haw_title = models.CharField(max_length=300)
    haw_issuer_organisation = models.CharField(max_length=300)
    haw_associated_organisation = models.CharField(max_length=300, null=True, blank=True)
    haw_start_date = models.DateField(auto_now=False, auto_now_add=False)
    haw_short_description = models.CharField(max_length=300)
    haw_description = models.TextField(null=True, blank=True)



## CertificatesCoursesTrainings model
def get_CertificationsCoursesTrainings_upload_path(instance, filename):
    """Generate a dynamic path for storing images."""
    app_directory = os.path.dirname(os.path.abspath(__file__))
    original_filename = os.path.basename(filename)
    print(app_directory, filename, original_filename)
    # return os.path.join(app_directory, 'staticfiles', 'myresources', f'project_{instance.pk}', filename)
    return os.path.join(app_directory, 'staticfiles', 'myresources', 'courseandcertificate', original_filename)

class CertificationsCoursesTrainings(models.Model):
    CERTIFICATION_TYPE_CHOICES = [
        ('all', 'All'),
        ('certificate', 'Certificate'),
        ('training', 'Training'),
        ('course', 'Course'),
        ('conference', 'Conference'),
        ('bootcamp', 'Bootcamp'),
    ]
    cct_name = models.CharField(max_length=300)
    cct_description = models.TextField(null=True, blank=True)
    cct_type = MultiSelectField(choices=CERTIFICATION_TYPE_CHOICES, default='all')
    cct_offering_organisation = models.CharField(max_length=300)
    cct_funding_organisation = models.CharField(max_length=300, null=True, blank=True)
    cct_key_information = models.TextField(null=True, blank=True)
    cct_hasexpire = models.BooleanField()
    cct_serial_no = models.IntegerField()
    cct_start_date = models.DateField(auto_now=False, auto_now_add=False)
    cct_end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    cct_image = models.ImageField(upload_to=get_CertificationsCoursesTrainings_upload_path, max_length=500, blank=True, null=True)
    cct_online_credential = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return f"{self.cct_name}, {self.cct_offering_organisation}, {self.cct_key_information}"


## Projects model
def get_organisation_upload_path(instance, filename):
    """Generate a dynamic path for storing images."""
    app_directory = os.path.dirname(os.path.abspath(__file__))
    original_filename = os.path.basename(filename)
    print(app_directory, filename, original_filename)
    # return os.path.join(app_directory, 'staticfiles', 'myresources', f'project_{instance.pk}', filename)
    return os.path.join(app_directory, 'staticfiles', 'myresources', 'organisations', original_filename)

class Projects(models.Model):
    project_position = models.CharField(max_length=150)
    project_title = models.CharField(max_length=300)
    project_description = models.TextField(null=True, blank=True)
    project_fund = models.CharField(max_length=300, null=True, blank=True)
    project_funding_organisation = models.CharField(max_length=500, null=True, blank=True)
    project_collaboration_organisation = models.CharField(max_length=500, null=True, blank=True)
    project_start_date = models.DateField(auto_now=False, auto_now_add=False)
    project_end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    # project_images = models.CharField(max_length=500)
    project_image = models.ImageField(upload_to=get_organisation_upload_path, max_length=500, blank=True, null=True)

    # def save_images(self, images):
    #     """Handles the saving of one or more images as JSON."""
    #     image_paths = []
    #     for image in images:
    #         file_path = get_organisation_upload_path(self, image.name)
    #         with open(file_path, 'wb+') as destination:
    #             for chunk in image.chunks():
    #                 destination.write(chunk)
    #         image_paths.append(file_path)
    #     self.images = json.dumps(image_paths)
    #     self.save()
    #
    # def get_images(self):
    #     """Return the list of image paths."""
    #     if self.images:
    #         return json.loads(self.images)
    #     return []
    def __str__(self):
        return f"{self.project_position}, {self.project_title}, {self.project_fund}, {self.project_collaboration_organisation}"


## Memberships model
class Memberships(models.Model):
    # membership_id = models.AutoField(primary_key=True)
    membership_name = models.CharField(max_length=150)
    membership_type = models.CharField(max_length=150)
    membership_organisation = models.CharField(max_length=500)
    membership_institution = models.CharField(max_length=500)
    membership_address = models.CharField(max_length=500)
    membership_hasexpire = models.BooleanField()
    membership_start_date = models.DateField(auto_now=False, auto_now_add=False)
    membership_end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    def __str__(self):
        return f"{self.membership_name}, {self.membership_type}, {self.membership_organisation}, {self.membership_institution}, {self.membership_address}"


## SessionsOrEvents model
class SessionsOrEvents(models.Model):
    session_lead_name = models.CharField(max_length=150)
    session_lead_type = models.CharField(max_length=150)
    session_title = models.CharField(max_length=500)
    session_description = models.TextField(null=True, blank=True)
    session_organisation = models.CharField(max_length=500)
    session_institution = models.CharField(max_length=500)
    session_address = models.CharField(max_length=500)
    session_start_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return f"{self.session_lead_name}, {self.session_lead_type}, {self.session_title}, {self.session_institution}, {self.session_address}"


## Languages model
class Languages(models.Model):
    language_name = models.CharField(max_length=150)
    language_description = models.CharField(max_length=500)
    language_test_details = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.language_name}, {self.language_description}, {self.language_test_details}"


## Languages model
class Portfolios(models.Model):
    portflio_platform_name = models.CharField(max_length=150)
    portflio_title = models.CharField(max_length=500)
    portflio_description = models.TextField(blank=True, null=True)
    portflio_link = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.portflio_platform_name}, {self.portflio_title}, {self.portflio_description}, {self.portflio_link}"


# Volunteering model
def get_Volunteering_upload_path(instance, filename):
    """Generate a dynamic path for storing images."""
    app_directory = os.path.dirname(os.path.abspath(__file__))
    original_filename = os.path.basename(filename)
    print(app_directory, filename, original_filename)
    # return os.path.join(app_directory, 'staticfiles', 'myresources', f'project_{instance.pk}', filename)
    return os.path.join(app_directory, 'staticfiles', 'myresources', 'volunteering', original_filename)

## Volunteering model
class Volunteering(models.Model):
    # membership_id = models.AutoField(primary_key=True)
    volunteering_name = models.CharField(max_length=150)
    volunteering_involvement = models.CharField(max_length=150)
    volunteering_cause = models.CharField(max_length=150)
    volunteering_organisation = models.CharField(max_length=500)
    volunteering_start_date = models.DateField(auto_now=False, auto_now_add=False)
    volunteering_end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    volunteering_detail = models.TextField(null=True, blank=True)
    volunteering_image = models.ImageField(upload_to=get_Volunteering_upload_path, max_length=500, blank=True,
                                  null=True)
    volunteering_link = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.volunteering_name}, {self.volunteering_cause}, {self.volunteering_organisation}"


## Publications model
class Publications(models.Model):
    pub_type = models.CharField(max_length=300)
    pub_subtype = models.CharField(max_length=300, null=True, blank=True)
    pub_title = models.CharField(max_length=500)
    pub_citation = models.CharField(max_length=1000)
    pub_doi_or_link = models.CharField(max_length=500)
    pub_serial_no = models.IntegerField()
    pub_abstract = models.TextField(null=True, blank=True)


## Publications model
class Contacts(models.Model):
    con_loc = models.CharField(max_length=300)
    con_email = models.CharField(max_length=300, null=True, blank=True)
    con_skype = models.CharField(max_length=500, null=True, blank=True)
    con_phone = models.CharField(max_length=100, null=True, blank=True)
    con_map_link = models.CharField(max_length=500)






