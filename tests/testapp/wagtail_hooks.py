from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from .models import TestModel


class TestModelAdmin(ModelAdmin):
    list_filter = (
        ("date_time_1", DateRangeFilter),
        ("date_time_2", DateTimeRangeFilter),
    )
    list_display = (
        "__str__",
        "date_time_1",
        "date_time_2",
    )
    model = TestModel


modeladmin_register(TestModelAdmin)
