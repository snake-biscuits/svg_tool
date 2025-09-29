# https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element
from __future__ import annotations
import re
from typing import List

from lxml import etree

# from ..utils import colour
from ..utils import physics2d
from ..utils import vector


# TODO: Unit class (px vs. %age)
# TODO: Gradients (linear & radial)


class Style:
    fill: str = "transparent"
    stroke: str = "black"
    thickness: str

    def __init__(self, fill=None, stroke=None, thickness=None):
        # TODO: colour.sRGB.from_css() all colours
        self.fill_colour = self.fill_colour if fill is None else fill
        self.stroke_colour = self.stroke_colour if stroke is None else stroke
        self.thickness = self.thickness if thickness is None else thickness

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Style:
        attribs = tag.attrib
        return cls(
            attribs.get("fill", None),
            attribs.get("stroke", None),
            attribs.get("stroke-width", None))


# NOTE: transform-origin also exists
# -- overriden by CSS property
# -- unavailable in Safari
class Transform:
    # list of functions; order of operations matters
    # matrix: List[float]  # matrix(a b c d e f)
    # 1st 2 rows of a 3x3 (last row is [0 0 1])
    # rotation: float  # rotate(a [x y]); angle + origin
    # scale: vector.vec2  # scale(x [y]); y=x
    # skew: vector.vec2  # skewX(A), skewY(a)
    # translation: vector.vec2  # translate(x [y]); y=0

    # TODO: apply to a shape

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Transform:
        raise NotImplementedError()


class Shape:
    style: Style
    transform: Transform
    bounds: physics2d.Bounds  # @property

    def __init__(self):
        self.style = Style()
        self.tranform = Transform()
        self.bounds = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} @ 0x{id(self):016X}>"

    def __str__(self) -> str:
        etree.to_string(self.as_xml())

    def as_xml(self) -> etree.Element:
        raise NotImplementedError()

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Shape:
        out = cls()
        out.style = Style.from_xml(tag)
        out.transform = Transform.from_xml(tag)
        return out


class ViewBox:  # abe.TokenClass
    number = r"[+-]?[0-9]*(\.[0-9]+)?([eE][+-]?[0-9]+)?"
    pattern = re.compile(",? ".join((number,)*4))
    top_left: vector.vec2
    size: vector.vec2

    def __init__(self, x, y, width, height):
        self.top_left = vector.vec2(x, y)
        self.size = vector.vec2(width, height)

    def as_bounds(self) -> physics2d.AABB:
        return physics2d.AABB.from_mins_maxs(
            self.top_left, self.top_left + self.size)

    @classmethod
    def from_string(cls, string: str) -> ViewBox:
        match = cls.pattern.match(string)
        assert match is not None
        return cls.from_tokens(match.groups())

    @classmethod
    def from_tokens(cls, tokens: List[str]) -> ViewBox:
        return cls(*map(float, tokens[::3]))
