from __future__ import annotations
import enum
from typing import List

from lxml import etree

from ..utils import physics2d
from . import base
from . import circle
from . import path
from . import poly
from . import rect


def shape_of(tag: etree.Element) -> base.Shape:
    classes = {
        cls.tag: cls
        for cls in (
            circle.Circle,
            circle.Ellipse,
            path.Line,
            path.Path,
            poly.Polygon,
            poly.Polyline,
            rect.Rect)}
    return classes[tag.tag].from_xml(tag)


class Gradient:
    # TODO
    ...


class MaskType(enum.Enum):
    LUMINANCE = 0  # default
    ALPHA = 1


class Mask:
    type: MaskType
    view_box: base.ViewBox
    shapes: List[base.Shape]

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Mask:
        attribs = tag.attrib
        out = cls()
        out.shapes = [
            shape_of(child)
            for child in tag
            if not isinstance(child, etree._Comment)]
        out.type = {
            "luminance": MaskType.LUMINANCE,
            "alpha": MaskType.ALPHA
        }[attribs.get("mask-type", "luminance")]
        # NOTE: can't just convert a %age to float
        # -- need to know parent's ViewBox to apply a %age
        x = float(attribs.get("x", "-10%"))
        y = float(attribs.get("y", "-10%"))
        width = float(attribs.get("width", "120%"))
        height = float(attribs.get("height", "120%"))
        out.view_box = base.ViewBox(x, y, width, height)
        return out


class Svg:
    viewBox: physics2d.AABB()
    shapes: List[base.Shape]  # layers?
    # TODO: elementById method
    # TODO: elementByClass method
    # TODO: stylesheet
    # TODO: cascading attribs (<g> etc.)
    # -- styles
    # -- transforms
    # -- mask

    def __init__(self):
        self.view_box = physics2d.AABB()
        self.shapes = list()

    def __repr__(self) -> str:
        descriptor = f"{len(self.shapes)} shapes"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    def as_xml(self) -> etree.Element:
        raise NotImplementedError()

    @property
    def bounds(self) -> physics2d.AABB:
        if self.viewBox != physics2d.AABB():
            return self.viewBox
        return sum(
            [shape.bounds for shape in self.shapes],
            start=physics2d.AABB())

    @classmethod
    def from_file(cls, filepath: str):
        return cls.from_xml(etree.parse(filepath).getroot())

    @classmethod
    def from_xml(cls, tag: etree.Element) -> Svg:
        out = cls()
        if "viewBox" in tag.attrib:
            args = list(map(float, tag.attrib["viewBox"].split(" ")))
            assert len(args) == 4
        # TODO:
        # -- <style> -> self.stylesheets.append
        # -- <script> -> content / href; preserved, but not executed
        # -- attribs
        # -- child shapes (subclass collection)
        raise NotImplementedError()
        return out
