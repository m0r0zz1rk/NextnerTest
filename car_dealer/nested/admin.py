import nested_admin

from django.contrib import admin

from nested.models import Auto, AutoBrand, AutoCharacters


class AutoCharactersInline(nested_admin.NestedStackedInline):
    model = AutoCharacters


class AutoInline(nested_admin.NestedStackedInline):
    model = Auto
    inlines = [AutoCharactersInline]


@admin.register(AutoBrand)
class TableOfBrandsAdmin(nested_admin.NestedModelAdmin):
    inlines = [AutoInline]
