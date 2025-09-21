from __future__ import annotations
from typing import List, Tuple

from lxml import etree

from . import base


class Path(base.Tag):
    route: Route

    def __init__(self, *args, route=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.route = Route() if route is None else route

    @classmethod
    def from_xml(cls, element: etree.Element) -> Path:
        out = super().from_xml(element)
        d = element.get("d", "")
        out.route = Route.from_string(d)
        return out


class Route:
    """<path d="..."> representation"""
    instructions = List[Tuple[str, float]]
    # ^ [("OpCode", *operands)]

    def __init__(self, instructions=None):
        self.instructions = list() if instructions is None else instructions

    @classmethod
    def from_string(cls, raw: str) -> Route:
        out = cls()
        # TODO: parse 1 char at a time, extracting opcodes & operands
        # -- fill area (path might not be a closed loop)
        # -- `L` to start from last (x,y)
        # --- shapes can be concave! break into simple AABBs first!
        # --- e.g. "left" of segment A in AABB A1
        # -- lowercase for relative movements
        raise NotImplementedError()
        return out
