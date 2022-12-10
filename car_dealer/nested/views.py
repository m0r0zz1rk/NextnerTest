from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView
from nested_formset import nestedformset_factory

from nested.models import Auto, AutoCharacters, AutoBrand


class StartPageView(View):
    """Стартовая страница с выбором автомобиля"""
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        brands = AutoBrand.objects.all()
        return render(request, self.template_name, {'brands': brands})


class EditAutoView(UpdateView):
    """Изменение характеристик автомобиля с помощью nested-formset"""
    model = AutoBrand
    template_name = 'edit.html'
    fields = "__all__"
    success_url = 'http://localhost/'

    def form_valid(self, formset):
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, formset):
        return self.render_to_response(self.get_context_data(formset=formset))

    def get_form_class(self):
        return nestedformset_factory(
            AutoBrand,
            Auto,
            nested_formset=inlineformset_factory(
                Auto,
                AutoCharacters,
                fields="__all__"
            )
        )

    def get_context_data(self, **kwargs):
        context = super(EditAutoView, self).get_context_data()
        context['brand'] = AutoBrand.objects.get(id=self.kwargs['pk'])
        return context

