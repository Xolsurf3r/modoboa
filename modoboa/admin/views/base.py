"""Admin views."""

from __future__ import unicode_literals

from django.views import generic

from django.contrib.auth import mixins as auth_mixins


class AdminIndexView(auth_mixins.LoginRequiredMixin, generic.TemplateView):
    """Admin index view."""

    template_name = "admin/index.html"
