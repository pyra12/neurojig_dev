from __future__ import annotations

from NeuroJig.core.model.models import ClipHolder, ConnectorHolder, Edge, Splice


def validate_edge_length(edge: Edge) -> None:
    """Ensure edge length is positive."""
    if edge.length <= 0:
        raise ValueError("Edge length must be > 0")


def validate_connector_holder(ch: ConnectorHolder, edge: Edge) -> None:
    """Check connector holder placement along the given edge."""
    if ch.distance_from_node < 0:
        raise ValueError("distance_from_node must be >= 0")
    if ch.node_id not in {edge.node_a_id, edge.node_b_id}:
        raise ValueError("ConnectorHolder node_id must belong to the edge")


def validate_clip_holder(ch: ClipHolder, edge: Edge) -> None:
    """Validate clip holder position along an edge."""
    if not 0 <= ch.pos_on_edge <= 1:
        raise ValueError("pos_on_edge must be between 0 and 1")
    # offset_perp is freeform but existence ensures value used
    _ = ch.offset_perp


def validate_splice(splice: Splice, edge: Edge) -> None:
    """Validate splice placement and cavities count."""
    if splice.edge_id != edge.id:
        raise ValueError("Splice edge_id must match edge")
    if splice.cavities <= 0:
        raise ValueError("Splice cavities must be > 0")
