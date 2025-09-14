"""In-memory project persistence service."""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import Optional, Union

from NeuroJig.core.model.models import Project
from NeuroJig.data.io_json import load_project, save_project


class ProjectService:
    """Simple service managing a single current project."""

    def __init__(self) -> None:
        self._project: Optional[Project] = None

    def create_project(self, name: str) -> Project:
        project = Project(id=str(uuid.uuid4()), name=name)
        self._project = project
        return project

    def get_project(self) -> Optional[Project]:
        return self._project

    def save_to_json(self, path: Union[str, Path]) -> None:
        if self._project is None:
            raise ValueError("No project to save")
        save_project(self._project, path)

    def load_from_json(self, path: Union[str, Path]) -> Project:
        project = load_project(path)
        self._project = project
        return project

    def clear(self) -> None:
        self._project = None
