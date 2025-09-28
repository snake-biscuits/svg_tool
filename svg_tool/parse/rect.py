from __future__ import annotations

from ..utils import physics2d
from ..utils import vector
from . import base

from lxml import etree


class Rect(base.Shape):
    tag = "rect"
    top_left: vector.vec2 = vector.vec2(0, 0)
    size: vector.vec2 = vector.vec2(0, 0)
    radii: vector.vec2 = vector.vec2(0, 0)

    def __init__(self, top_left=None, size=None, radii=None):
        super().__init__()
        self.top_left = self.top_left if top_left is None else top_left
        self.size = self.size if size is None else size
        self.radii = self.radii if radii is None else radii

    @property
    def bounds(self):
        # TODO: use Circle for corners if radii != (0, 0)
        # -- can have a second AABB for the ambiguous region
        # -- since rx might not match ry, it could get complicated
        # -- or we need some kind of dot product weighting
        # NOTE: circle.Ellipse exists, radiused corners are ellipses
        return physics2d.AABB.from_mins_maxs(
                self.top_left, self.top_left + self.size)

    @classmethod
    def from_xml(cls, element: etree.Element) -> Rect:
        out = super().from_xml(element)
        attribs = element.attrib
        if "x" in attribs and "y" in attribs:
            out.top_left = vector.vec2(attribs["x"], attribs["y"])
        if "width" in attribs and "height" in attribs:
            out.size = vector.vec2(attribs["width"], attribs["height"])
        if "rx" in attribs and "ry" in attribs:
            out.radii = vector.vec2(attribs["rx"], attribs["ry"])
        return out
