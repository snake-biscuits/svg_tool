__all__ = [
    "base", "cie", "ok", "srgb", "x11",
    "Colour",
    "CIELab", "CIELch", "CIEXYZ",
    "OkLab", "OkLch", "OkLMS",
    "LinearRGB", "sRGB",
    "hex_names", "named_colours"]

from . import base
from . import cie
from . import ok
from . import srgb
# from . import tv
from . import x11

from .base import Colour
from .cie import Lab as CIELab
from .cie import Lch as CIELch
from .cie import XYZ as CIEXYZ
from .ok import Lab as OkLab
from .ok import Lch as OkLch
from .ok import LMS as OkLMS
from .srgb import LinearRGB, sRGB
# from .tv import YUV, YDbDr, YIQ, YPbPr, YCbCr
# from .tv import YUV as PAL
# from .tv import YDbDr as SECAM
# from .tv import YIQ as NTSC
# from .tv import YPbPr as Component  # Analog
# from .tv import YCbCr as DigitalComponent  # JPEG / MPEG
from .x11 import hex_names, named_colours

# TODO: monkey patch cross-script methods onto ColourClasses
# -- x11:
# --- .from_string()  # "name", "#hex", "func(args)"
# -- cie, ok, srgb:
# -- .as_ColourSpace(self)  # OkLab, sRGB, XYZ etc.
# -- .from_ColourSpace(cls, src)  # @classmethod
# NOTE: we can chain methods to recycle code

# TODO: 1xluma + 2xchroma luma curve func (also LinearRGB)
# -- this could be handy for colour correction (LUTs)
# TODO: breki.BinaryFile `.raw` (reSource CC LUT)

# TODO: visualiser
# -- handy for debugging / validating
# -- DearPyGui graphs
# -- PyOpenGL 3D representation
