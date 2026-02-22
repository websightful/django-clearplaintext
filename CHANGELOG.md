# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Utility function `render_to_plaintext` that renders a Django template via `render_to_string` and applies `clean_plaintext` normalization to the result.

## [v1.1.0] - 2026-02-21

### Added

- Template filter `keep_whitespace` to preserve whitespace in values from the database within the `clean_plaintext` filter block.

## [v1.0.2] - 2026-02-21

### Changed

- Module name changed for the build with uv_build.

## [v1.0.1] - 2026-02-21

### Changed

- Project description updated for the build.

## [v1.0.0] - 2026-02-21

### Added

- Initial release of `django-clearplaintext` with template filter `clean_plaintext` that collapses real whitespace to single spaces, preserves escaped sequences (`\n`, `\t`, `\s`), removes extra whitespace between control characters (`\n`, `\t`), and ignores template indentation.  
- Includes tests covering escaped newlines, tabs, and spaces, leading/trailing spaces, and combinations of real whitespace and escaped sequences.  
- `tox` setup to test against multiple Django versions.

<!--
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->
