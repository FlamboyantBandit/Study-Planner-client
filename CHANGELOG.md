# Changelog

All notable changes to this project will be documented here.

## [Unreleased]

### Fixed
- Fixed crash in `add_task` when the task list is empty (caused by `max()` being called on an empty sequence)
- Fixed `mark_complete` always returning after checking the first task regardless of whether it matched, due to misindented `return` statement
- Fixed typo in "Date of Completion" input prompt (`DD-MM-YYYy` → `DD-MM-YYYY`)

## [0.1.0] - 2026-03-19

### Added
- `tasks_manager.py` with full task operations: load, save, add, view, complete, and delete
- `main.py` as the CLI entry point with an interactive menu loop
- `planner.json` as local task storage file
- `.gitignore` to exclude `planner.json` from version control

### Notes
- Initial working version of the Smart Study Planner CLI
