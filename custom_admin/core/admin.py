from django.contrib import admin
from .models import TV, Dishwasher, Notebook, Brand, Category, VacuumCleaner, Promo


for model in [TV, Notebook, Category, VacuumCleaner, Promo]:
    admin.site.register(model)


class DishwasherInstanceInline(admin.TabularInline):
    model = Dishwasher

# с помощью данного класса есть возможность изменять сразу несколько инстансов модели
# которые подвязаны под данную модель
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [DishwasherInstanceInline]

@admin.register(Dishwasher)
class DishwasherAdmin(admin.ModelAdmin):

    list_display = ('model', 'brand_name', 'price', 'color', 'test_show_promo', 'colored_name')
    list_filter = ('price', 'brand_name', 'color')  # для добавления возможности фильтровать по указанным параметрам объекты таблицы

    # для разбития полей по колонка непоредственно уже внтри объекта (более простой вариант)
    # fields = [('model', 'brand_name'), ('price', 'color'),]

    # для разбития полей по колонка непоредственно уже внтри объекта (более качественный вариант)
    # fieldsets = (
    #     ('General info', {
    #         'fields': ('brand_name', 'model'),
    #     }),
    #     ('Advanced options', {
    #         'fields': ('price', 'color'),
    #     }),)

    sortable_by = 'price' # для сортировки в данном случае по цене
    search_fields = ['model'] # добавления возможности поиска по указанному атрибуту

    empty_value_display = '-без бренда-'
    readonly_fields = ('price',)  # убираем возможность менять поле из админки

    # test_show_promo для возможности изпользовать м2м поля в list_display отображения списков
    def test_show_promo(self, obj):
        return obj.promo
