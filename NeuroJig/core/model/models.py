from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from pydantic import BaseModel, Field, validator, conlist


class Node(BaseModel):
    id: str
    x: float
    y: float
    pinned: bool = False
    connected_edge_ids: List[str] = Field(default_factory=list)


class Edge(BaseModel):
    id: str
    node_a_id: str
    node_b_id: str
    length: float
    active: bool = True
    adjacency_limits: Optional[Dict[str, Any]] = None

    @validator("length")
    def length_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("length must be > 0")
        return v


class AngleConstraint(BaseModel):
    id: str
    node_a: str
    node_b: str
    node_c: str
    value_deg: float
    locked: bool = False


class BaseElement(BaseModel):
    id: str
    asset_ref: str
    code_app: Optional[str] = None


class ConnectorHolder(BaseElement):
    node_id: str
    distance_from_node: float
    width: float
    height: float

    @validator("distance_from_node")
    def distance_non_negative(cls, v: float) -> float:
        if v < 0:
            raise ValueError("distance_from_node must be >= 0")
        return v


class ClipHolder(BaseElement):
    edge_id: str
    pos_on_edge: float
    offset_perp: float
    size: float

    @validator("pos_on_edge")
    def pos_in_range(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("pos_on_edge must be between 0 and 1")
        return v


class Splice(BaseElement):
    edge_id: str
    pos_on_edge: float
    cavities: int

    @validator("pos_on_edge")
    def splice_pos_in_range(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("pos_on_edge must be between 0 and 1")
        return v

    @validator("cavities")
    def cavities_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("cavities must be > 0")
        return v


class GrommetHolder(BaseElement):
    edge_id: str
    pos_on_edge: float
    width: float
    height: float

    @validator("pos_on_edge")
    def grommet_pos_in_range(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError("pos_on_edge must be between 0 and 1")
        return v


class ConnectorType(BaseModel):
    id: str
    name: str
    CPN: str
    YPN: str
    cavities: int
    dims: Optional[Tuple[float, float]] = None

    @validator("cavities")
    def connector_cavities_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("cavities must be > 0")
        return v


class SpliceType(BaseModel):
    id: str
    CPN: str
    YPN: str
    cavities: Dict[str, int]


class ClipType(BaseModel):
    id: str
    CPN: str
    YPN: str
    tie_strap_len: Optional[float] = None


class GrommetType(BaseModel):
    id: str
    name: str
    CPN: str
    YPN: str


class Circuit(BaseModel):
    id: str
    SN: str
    length: Optional[float] = None
    section: float
    colors: conlist(str, min_length=1, max_length=2)
    terminal1: Optional[str] = None
    terminal2: Optional[str] = None
    endpoint1: Dict[str, Any]
    endpoint2: Dict[str, Any]
    path_edges: List[str]
    valid_path: bool = True
