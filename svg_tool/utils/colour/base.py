from __future__ import annotations
from typing import List

import math


class Colour:
    # 3x channels per-implementation + alpha
    # NOTE: most channels range from 0 -> 1
    # -- however, some colour spaces eclipse sRGB
    # -- not doing any math or asserts to clamp to valid sRGB atm
    # NOTE: polar hue channels use a 0 -> 360 range
    alpha: float

    # _channels = [..., "alpha"]

    def __init__(self, *args, alpha=1, **kwargs):
        # TODO: move asserts to tests/ `ColourClass.test_spec`
        assert len(self._channels) == 4
        assert self._channels[-1] == "alpha"
        # get attrs
        channels = {"alpha": alpha}
        channels.update({
            attr: value
            for attr, value in zip(self._channels, args)})
        channels.update(kwargs)
        assert all(channel in channels for channel in self._channels)
        # TODO: use set.difference to tell user which channels are missing
        for attr, value in channels.items():
            setattr(self, attr, value)

    def __repr__(self) -> str:
        arg_strs = list(map(str, self[:3]))
        if self.alpha != 1:
            arg_strs.append(f"alpha={self.alpha}")
        args = ", ".join(arg_strs)
        return f"{self.__class__.__name__}({args})"

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        return False

    def __getitem__(self, index):
        return list(self)[index]

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self):
        return iter([
            getattr(self, channel)
            for channel in self._channels])

    def __len__(self):
        return 4

    def as_polar(self) -> List[float]:
        """Lab/UV -> Lch"""
        L, a, b, alpha = self
        chroma = math.sqrt(a ** 2 + b ** 2)
        hue = math.degrees(math.atan2(b, a))
        return (L, chroma, hue, alpha)

    def as_cartesian(self) -> List[float]:
        """Lch -> Lab/UV"""
        L, chroma, hue, alpha = self
        a = chroma * math.cos(math.radians(hue))
        b = chroma * math.sin(math.radians(hue))
        return (L, a, b, alpha)
