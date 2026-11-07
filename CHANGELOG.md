# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [1.1.0] - 2026-11-08
### Added
- Sorting methods for Cart: `sort_by_title()` and `sort_by_cost()`.
- DVD category search functionality (`search_by_category`).

## [1.0.0] - 2026-11-07
### Added
- Cart management with DVD addition, removal, and cost calculation.
- Formatted cart display via `print_cart()`.
- DVD title search functionality (`search_by_title`).

### Fixed
- Reject DVD additions beyond maximum capacity of 20 (Issue #6).