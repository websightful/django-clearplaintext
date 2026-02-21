# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
