# Wagtail Rangefilter Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

-

## [0.2.1] - 2024-02-07

- Fixed DateTimeRangeFilter for django-admin-rangefilter >= 0.12.
- Changed required django-admin-rangefilter to 0.12 and above.
- Adapted tests against Wagtail >= 6.0 due to removed `wagtail.contrib.modeladmin`
- Added tests against Wagtail 5.1, 5.2 (by @lparsons396, @katdom13)
- Drop tests for Wagtail 4.2, 5.0 and Django 4.1 as they have reached EOL (@katdom13, @th3hamm0r)

## [0.2.0] - 2023-07-31

### Added

- Added support for Wagtail 5.0, Django 4.2, and Python 3.11 (by @katdom13)

### Removed

- Removed support for Wagtail < 4.1, Django 4.0, and Python 3.7 (by @katdom13)

## [0.1.1] - 2022-12-05

### Changed

- Improved buttons (#1) by @kevinhowbrook
- Improved testing and docs

## [0.1.0] - 2022-09-20

Initial release

<!-- TEMPLATE - keep below to copy for new releases -->
<!--


## [x.y.z] - YYYY-MM-DD

### Added

- ...

### Changed

- ...

### Removed

- ...

-->


[0.2.1]: https://github.com/wunderweiss/wagtail-rangefilter/releases/tag/v0.2.1
[0.2.0]: https://github.com/wunderweiss/wagtail-rangefilter/releases/tag/v0.2.0
[0.1.1]: https://github.com/wunderweiss/wagtail-rangefilter/releases/tag/v0.1.1
[0.1.0]: https://github.com/wunderweiss/wagtail-rangefilter/releases/tag/v0.1.0
