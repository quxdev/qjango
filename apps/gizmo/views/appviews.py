from django.views.generic import TemplateView

from qux.seo.mixin import SEOMixin


class ApplicationHomeView(SEOMixin, TemplateView):
    template_name = "gizmo/index.html"
