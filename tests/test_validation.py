import pytest

from NeuroJig.core.model.models import ClipHolder, ConnectorHolder, Edge, Splice
from NeuroJig.services.validation import (
    validate_clip_holder,
    validate_connector_holder,
    validate_edge_length,
    validate_splice,
)


def test_validate_edge_length_valid():
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    validate_edge_length(edge)


def test_validate_edge_length_invalid():
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    edge.length = 0
    with pytest.raises(ValueError):
        validate_edge_length(edge)


def test_validate_connector_holder_valid():
    ch = ConnectorHolder(
        id="c1",
        asset_ref="conn",
        node_id="n1",
        distance_from_node=1.0,
        width=1.0,
        height=1.0,
    )
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    validate_connector_holder(ch, edge)


def test_validate_connector_holder_invalid():
    ch = ConnectorHolder(
        id="c1",
        asset_ref="conn",
        node_id="n1",
        distance_from_node=1.0,
        width=1.0,
        height=1.0,
    )
    ch.node_id = "n3"
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    with pytest.raises(ValueError):
        validate_connector_holder(ch, edge)


def test_validate_clip_holder_valid():
    ch = ClipHolder(
        id="cl1",
        asset_ref="clip",
        edge_id="e1",
        pos_on_edge=0.5,
        offset_perp=0.0,
        size=1.0,
    )
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    validate_clip_holder(ch, edge)


def test_validate_clip_holder_invalid():
    ch = ClipHolder(
        id="cl1",
        asset_ref="clip",
        edge_id="e1",
        pos_on_edge=0.5,
        offset_perp=0.0,
        size=1.0,
    )
    ch.pos_on_edge = 2.0
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    with pytest.raises(ValueError):
        validate_clip_holder(ch, edge)


def test_validate_splice_valid():
    sp = Splice(id="s1", asset_ref="sp", edge_id="e1", pos_on_edge=0.5, cavities=2)
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    validate_splice(sp, edge)


def test_validate_splice_invalid():
    sp = Splice(id="s1", asset_ref="sp", edge_id="e1", pos_on_edge=0.5, cavities=2)
    sp.cavities = 0
    edge = Edge(id="e1", node_a_id="n1", node_b_id="n2", length=1.0)
    with pytest.raises(ValueError):
        validate_splice(sp, edge)
