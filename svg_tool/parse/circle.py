from ..utils import physics2d
from ..utils import vector
from . import base


class Circle(base.Shape):
    tag = "circle"
    origin: vector.vec2
    radius: float

    def __init__(self, cx, cy, r):
        super().__init__()
        self.origin = vector.vec2(cx, cy)
        self.radius = r

    @property
    def bounds(self) -> physics2d.Circle:
        return physics2d.Circle(self.origin, self.radius)


class Ellipse(base.Shape):
    tag = "ellipse"
    origin: vector.vec2
    radius: vector.vec2

    def __init__(self, cx, cy, rx, ry):
        super().__init__()
        self.origin = vector.vec2(cx, cy)
        self.radius = vector.vec2(rx, ry)

    @property
    def bounds(self):
        return physics2d.AABB.from_origin_extents(self.origin, self.radius)
        # NOTE: physics2d.Circle(self.origin, max(self.radius))
        # -- this more accurate when rx & ry are close
        # -- an AABB will always be a loose fit, but its's consistent
        # TODO: physics2d.Ellipse
        # -- Circle w/ dot product bias (x/y radius weighting)
        # -- Honestly pretty simple vs 2 focii
        # NOTE: PIL.ImageDraw uses a minmax bounds to draw an ellipse
