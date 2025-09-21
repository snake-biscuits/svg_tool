from __future__ import annotations
from typing import List, Tuple

from lxml import etree

from . import base


# TODO: get children by id / class
# TODO: apply stylesheet (`*.css` parser)
class Svg:
    # TODO: attrs
    viewBox: Tuple[int, int, int, int]
    children: List[base.Tag]

    def __init__(self):
        # TODO: defaults
        self.view_box = (-1,) * 4
        # NOTE: using -1 to mean clip to bounds

    def __repr__(self) -> str:
        descriptor = ...
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self):016X}>"

    def as_xml(self) -> etree.Element:
        raise NotImplementedError()

    @property
    def size(self) -> (int, int):
        # TODO: viewBox -> (width, height)
        # -- calculate child bounds if -1 in viewBox
        raise NotImplementedError()

    @classmethod
    def from_xml(cls, element: etree.Element) -> Svg:
        out = cls()
        # TODO:
        # -- <style> -> self.stylesheet
        # -- <script> -> content / href; preserved, but not executed
        # -- attribs
        # -- children
        raise NotImplementedError()
        return out
