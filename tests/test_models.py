import pytest
from pydantic import ValidationError

from NeuroJig.core.model.models import (
    AngleConstraint,
    Circuit,
    ClipHolder,
    ClipType,
    ConnectorHolder,
    ConnectorType,
    Edge,
    GrommetHolder,
    GrommetType,
    Node,
    Splice,
    SpliceType,
)


def test_node_valid():
    node = Node(id="n1", x=0.0, y=1.0)
    assert node.id == "n1"


def test_node_invalid_type():
    with pytest.raises(ValidationError):
        Node(id="n1", x="a", y=0.0)


def test_edge_valid():
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    assert edge.length == 1.0


def test_edge_invalid_length():
    with pytest.raises(ValidationError):
        Edge(id="e1", node_a_id="n1", node_b_id="n2", length=0)


def test_angle_constraint_valid():
    ac = AngleConstraint(id="a1", node_a="n1", node_b="n2", node_c="n3", value_deg=45.0)
    assert ac.value_deg == 45.0


def test_angle_constraint_invalid():
    with pytest.raises(ValidationError):
        AngleConstraint(
            id="a1", node_a="n1", node_b="n2", node_c="n3", value_deg="forty"
        )


def test_connector_holder_valid():
    ch = ConnectorHolder(
        id="ch1",
        asset_ref="conn",
        node_id="n1",
        distance_from_node=0.5,
        width=10.0,
        height=5.0,
    )
    assert ch.distance_from_node == 0.5


def test_connector_holder_invalid_distance():
    with pytest.raises(ValidationError):
        ConnectorHolder(
            id="ch1",
            asset_ref="conn",
            node_id="n1",
            distance_from_node=-1.0,
            width=10.0,
            height=5.0,
        )


def test_clip_holder_valid():
    ch = ClipHolder(
        id="cl1",
        asset_ref="clip",
        edge_id="e1",
        pos_on_edge=0.5,
        offset_perp=1.0,
        size=2.0,
    )
    assert ch.pos_on_edge == 0.5


def test_clip_holder_invalid_pos():
    with pytest.raises(ValidationError):
        ClipHolder(
            id="cl1",
            asset_ref="clip",
            edge_id="e1",
            pos_on_edge=1.5,
            offset_perp=1.0,
            size=2.0,
        )


def test_splice_valid():
    sp = Splice(id="s1", asset_ref="sp", edge_id="e1", pos_on_edge=0.4, cavities=2)
    assert sp.cavities == 2


def test_splice_invalid_pos():
    with pytest.raises(ValidationError):
        Splice(id="s1", asset_ref="sp", edge_id="e1", pos_on_edge=2.0, cavities=2)


def test_grommet_holder_valid():
    gh = GrommetHolder(
        id="g1", asset_ref="gr", edge_id="e1", pos_on_edge=0.3, width=5.0, height=2.0
    )
    assert gh.width == 5.0


def test_grommet_holder_invalid_pos():
    with pytest.raises(ValidationError):
        GrommetHolder(
            id="g1",
            asset_ref="gr",
            edge_id="e1",
            pos_on_edge=-0.1,
            width=5.0,
            height=2.0,
        )


def test_connector_type_valid():
    ct = ConnectorType(
        id="ct1", name="Conn", CPN="c1", YPN="y1", cavities=3, dims=(1.0, 2.0)
    )
    assert ct.cavities == 3


def test_connector_type_invalid_cavities():
    with pytest.raises(ValidationError):
        ConnectorType(id="ct1", name="Conn", CPN="c1", YPN="y1", cavities=0)


def test_splice_type_valid():
    st = SpliceType(id="st1", CPN="c1", YPN="y1", cavities={"R": 1, "L": 1})
    assert st.cavities["R"] == 1


def test_splice_type_invalid_cavities():
    with pytest.raises(ValidationError):
        SpliceType(id="st1", CPN="c1", YPN="y1", cavities="invalid")


def test_clip_type_valid():
    ct = ClipType(id="cl1", CPN="c1", YPN="y1", tie_strap_len=10.0)
    assert ct.tie_strap_len == 10.0


def test_clip_type_invalid_type():
    with pytest.raises(ValidationError):
        ClipType(id="cl1", CPN="c1", YPN="y1", tie_strap_len="long")


def test_grommet_type_valid():
    gt = GrommetType(id="g1", name="Grom", CPN="c1", YPN="y1")
    assert gt.name == "Grom"


def test_grommet_type_invalid_missing():
    with pytest.raises(ValidationError):
        GrommetType(id="g1", name="Grom")


def test_circuit_valid():
    c = Circuit(
        id="c1",
        SN="SN1",
        length=10.0,
        section=0.5,
        colors=["red", "blue"],
        endpoint1={"type": "connector"},
        endpoint2={"type": "splice"},
        path_edges=["e1", "e2"],
    )
    assert c.valid_path is True


def test_circuit_invalid_colors():
    with pytest.raises(ValidationError):
        Circuit(
            id="c1",
            SN="SN1",
            section=0.5,
            colors=["r", "g", "b"],
            endpoint1={"type": "connector"},
            endpoint2={"type": "splice"},
            path_edges=["e1"],
        )
