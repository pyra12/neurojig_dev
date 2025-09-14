"""JSON serialization helpers for Project objects."""

from __future__ import annotations

from pathlib import Path
from typing import Union

from NeuroJig.core.model.models import Project


def save_project(project: Project, path: Union[str, Path]) -> None:
    p = Path(path)
    p.write_text(project.model_dump_json(indent=2))


def load_project(path: Union[str, Path]) -> Project:
    p = Path(path)
    return Project.model_validate_json(p.read_text())
