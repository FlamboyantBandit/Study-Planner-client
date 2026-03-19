# Changelog

All notable changes to this project will be documented here.

## [0.1.1] - 2026-03-19

### Fixed
- Fixed id starting with the one which was deleted when adding a new task in `add_task` (caused by `len()` returning duplicate ids)
- Fixed `view_task` which was asking for completion date instead of asking on completion, feature now added to `mark_complete`
- Fixed typo in "Date of Completion" input prompt (`DD-MM-YYY` → `DD-MM-YYYY`)

## [0.1.0] - 2026-03-19

### Added
- `tasks_manager.py` with full task operations: load, save, add, view, complete, and delete
- `main.py` as the CLI entry point with an interactive menu loop
- `planner.json` as local task storage file
- `.gitignore` to exclude `planner.json` from version control

### Notes
- Initial working version of the Smart Study Planner CLI
