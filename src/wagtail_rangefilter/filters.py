from django import forms
from django.utils.translation import gettext_lazy as _
from rangefilter.filters import (
    DateRangeFilter as BaseDateRangeFilter,
    DateTimeRangeFilter as BaseDateTimeRangeFilter,
)
from wagtail.admin.widgets import AdminDateInput, AdminDateTimeInput


class WagtailDateRangeMixin:
    def get_template(self):
        return "wagtail_rangefilter/date_filter.html"

    template = property(get_template)

    def _get_form_class(self: BaseDateRangeFilter):
        fields = self._get_form_fields()
        form_class = type(
            str("DateRangeForm"), (forms.BaseForm,), {"base_fields": fields}
        )
        return form_class


class DateRangeFilter(WagtailDateRangeMixin, BaseDateRangeFilter):
    def _get_form_fields(self):
        return {
            self.lookup_kwarg_gte: forms.DateField(
                label="",
                widget=AdminDateInput(attrs={"placeholder": _("From date")}),
                localize=True,
                required=False,
                initial=self.default_gte,
            ),
            self.lookup_kwarg_lte: forms.DateField(
                label="",
                widget=AdminDateInput(attrs={"placeholder": _("To date")}),
                localize=True,
                required=False,
                initial=self.default_lte,
            ),
        }


class DateTimeRangeFilter(WagtailDateRangeMixin, BaseDateTimeRangeFilter):
    def _get_expected_fields(self):
        # We don't use the SplitDateTimeField, therefore we use the DateRangeFilter's definition.
        return super(BaseDateTimeRangeFilter, self)._get_expected_fields()

    def _get_form_fields(self):
        return {
            self.lookup_kwarg_gte: forms.DateTimeField(
                label="",
                widget=AdminDateTimeInput(attrs={"placeholder": _("From date")}),
                localize=True,
                required=False,
                initial=self.default_gte,
            ),
            self.lookup_kwarg_lte: forms.DateTimeField(
                label="",
                widget=AdminDateTimeInput(attrs={"placeholder": _("To date")}),
                localize=True,
                required=False,
                initial=self.default_lte,
            ),
        }
