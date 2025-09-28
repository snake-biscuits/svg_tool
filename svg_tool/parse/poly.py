from __future__ import annotations
import re
from typing import List

from lxml import etree

from . import base
from ..utils import physics2d
from ..utils import vector


class Polyline(base.Shape):
    tag = "polyline"
    points: List[vector.vec2]

    def __init__(self):
        super().__init__()
        self.points = list()

    @property
    def bounds(self) -> physics2d.AABB:
        return physics2d.AABB.from_points(self.points)

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Polygon:
        number = r"[+-]?[0-9]*(\.[0-9]+)?([eE][+-]?[0-9]+)?"
        pattern = re.compile(f"{number}, {number} ?")
        out = super().from_xml(tag)
        out.points = [
            vector.vec2(*map(float, point.split(", ")))
            for point in pattern.findall(tag.attrib["points"])]
        return out


class Polygon(Polyline):
    tag = "polygon"

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Polygon:
        out = super().from_xml(tag)
        out.points.append(out.points[0])
        return out
