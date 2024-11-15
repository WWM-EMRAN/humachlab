from .models import SkillsAndTools, HonorsAndAwards, CertificationsCoursesTrainings, Projects, Memberships, SessionsOrEvents, Languages, Portfolios, Volunteering


def get_all_data_models():
    skills_and_tools = SkillsAndTools.objects
    honors_and_awards = HonorsAndAwards.objects.order_by('id').reverse()
    certifications_courses_trainings = CertificationsCoursesTrainings.objects#.order_by('id').reverse()
    projects = Projects.objects.order_by('id').reverse()
    memberships = Memberships.objects.order_by('id').reverse()
    sessions_or_events = SessionsOrEvents.objects.order_by('id').reverse()
    languages = Languages.objects
    portfolios = Portfolios.objects
    volunteering = Volunteering.objects
    all_data_models = {
        'skills_and_tools': skills_and_tools,
        'honors_and_awards': honors_and_awards,
        'certifications_courses_trainings': certifications_courses_trainings,
        'projects': projects,
        'memberships': memberships,
        'sessions_or_events': sessions_or_events,
        'languages': languages,
        'portfolios': portfolios,
        'volunteering': volunteering,
    }
    return all_data_models




