from NeuroJig.core.model.models import Edge, Node
from NeuroJig.data.store.project_service import ProjectService


def test_create_project():
    service = ProjectService()
    project = service.create_project("Demo")
    assert project.name == "Demo"
    assert service.get_project() is project


def test_save_and_load_project(tmp_path):
    service = ProjectService()
    project = service.create_project("Demo")
    project.nodes["n1"] = Node(id="n1", x=0.0, y=0.0)
    project.nodes["n2"] = Node(id="n2", x=1.0, y=0.0)
    project.edges["e1"] = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)

    path = tmp_path / "project.json"
    service.save_to_json(path)

    service.clear()
    assert service.get_project() is None

    loaded = service.load_from_json(path)
    assert loaded == project
    assert loaded.nodes["n1"].x == 0.0
