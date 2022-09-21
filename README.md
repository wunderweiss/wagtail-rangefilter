# Wagtail Rangefilter

[![PyPI](https://img.shields.io/pypi/v/wagtail-rangefilter)](https://pypi.org/project/wagtail-rangefilter/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Wagtail Rangefilter CI](https://github.com/wunderweiss/wagtail-rangefilter/actions/workflows/test.yml/badge.svg)](https://github.com/wunderweiss/wagtail-rangefilter/actions/workflows/test.yml)

Integrates [django-admin-rangefilter](https://pypi.org/project/django-admin-rangefilter/) into Wagtail's ModelAdmin

![Screenshot](https://raw.githubusercontent.com/wunderweiss/wagtail-rangefilter/main/.github/screenshot.png)

## Links

- [Documentation](https://github.com/wunderweiss/wagtail-rangefilter/blob/main/README.md)
- [Changelog](https://github.com/wunderweiss/wagtail-rangefilter/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/wunderweiss/wagtail-rangefilter/blob/main/CONTRIBUTING.md)

## Supported versions

- Python 3.7, 3.8, 3.9, 3.10
- Django 3.2, 4.0, 4.1
- Wagtail 2.15, 3.0, 4.0

## Installation

```shell
pip install wagtail-rangefilter
```

Add this to your installed django applications:
```python
INSTALLED_APPS = [
    ...,
    'wagtail_rangefilter',
    'rangefilter',
    ...,
]
```

## Example usage

```python
from wagtail.contrib.modeladmin.options import ModelAdmin
from wagtail_rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class ExampleAdmin(ModelAdmin):
    ...
    list_filter = (("test_date", DateRangeFilter), ("test_datetime", DateTimeRangeFilter),)
    ...

```

## Development

```shell
pip install -e '.[testing]' -U
```
