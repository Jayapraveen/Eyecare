from django.views.generic.base import TemplateView


class ChatterBotAppView(TemplateView):
    template_name = "app.html"

class appointment(TemplateView):
    template_name = "appointment.html"

class contact(TemplateView):
    template_name = "contact.html"

class doctor(TemplateView):
    template_name = "doctor.html"

