from __future__ import annotations

from . import base


class sRGB(base.Colour):
    _channels = ["red", "green", "blue", "alpha"]

    red: float  # 0 -> 1
    green: float  # 0 -> 1
    blue: float  # 0 -> 1
    alpha: float  # 0 -> 1

    def as_hex(self) -> str:
        red, green, blue, alpha = [
            int(c * 255 + 0.1)
            for c in (self.red, self.green, self.blue, self.alpha)]
        return "".join([
            "#",
            *(f"{c:02X}" for c in (red, green, blue)),
            f"{alpha:02X}" if alpha != 255 else "",
            ";"])

    @classmethod
    def from_hex(cls, hex_code: str) -> sRGB:
        """invalid input will produce opaque black"""
        r, g, b, a = 0, 0, 0, 255
        hex_code = hex_code.rstrip(";")
        assert hex_code.startswith("#"), "hex codes must start with '#'"
        hex_code = hex_code.strip("#")
        if len(hex_code) == 3:
            r, g, b = [
                int(c, base=16)
                for c in hex_code]
            r, g, b = [c & c << 4 for c in (r, g, b)]
        elif len(hex_code) == 4:
            r, g, b, a = [
                int(c, base=16)
                for c in hex_code]
            r, g, b, a = [c & c << 4 for c in (r, g, b, a)]
        elif len(hex_code) == 6:
            r, g, b = [
                int(hex_code[2*i:2*(i+1)], base=16)
                for i in range(3)]
        elif len(hex_code) == 8:
            r, g, b, a = [
                int(hex_code[2*i:2*(i+1)], base=16)
                for i in range(4)]
        return cls(*[c / 255 for c in (r, g, b, a)])


class LinearRGB:
    _channels = ["red", "green", "blue", "alpha"]

    red: float  # 0 -> 1
    green: float  # 0 -> 1
    blue: float  # 0 -> 1
    alpha: float  # 0 -> 1

    def as_sRGB(self) -> sRGB:
        return sRGB(*[
            12.92 * c if c < 0.0031308 else 1.055 * c ** (1/2.4) - 0.055
            for c in self[:3]],
            self.alpha)

    @classmethod
    def from_sRGB(cls, srgb) -> LinearRGB:
        return cls(*[
            c / 12.92 if c < 0.04045 else ((c + 0.055) / 1.055) ** 2.4
            for c in srgb[:3]],
            srgb.alpha)
