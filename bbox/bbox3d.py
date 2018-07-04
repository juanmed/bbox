import numpy as np
from pyquaternion import Quaternion


class BBox3D:
    """
    Class for 3D Bounding Boxes
    """

    def __init__(self, x, y, z, length, width, height, rx=0, ry=0, rz=0, rw=1, center=True):
        """
        For now we just take either the center of the 3D bounding box or the top-left-closer corner,
        and the width, height and length, and quaternion values.
        """
        if center:
            self._cx, self._cy, self._cz = x, y, z
            self._c = np.array([x, y, z])
        else:
            self._cx = x + length/2
            self._cy = y + width/2
            self._cz = z + height/2
            self._c = np.array([self._cx, self._cy, self._cz])

        self._w, self._h, self._l = width, height, length
        self._q = Quaternion(rw, rx, ry, rz)

    @property
    def center(self):
        return np.array([self._cx, self._cy, self._cz, 1])

    @property
    def cx(self):
        return self._cx

    @property
    def cy(self):
        return self._cy

    @property
    def cz(self):
        return self._cz

    @property
    def l(self):
        return self._l

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h

    @property
    def p1(self):
        p = np.array([-self._l/2, -self._w/2, -self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p2(self):
        p = np.array([self._l/2, -self._w/2, -self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p3(self):
        p = np.array([self._l/2, self._w/2, -self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p4(self):
        p = np.array([-self._l/2, self._w/2, -self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p5(self):
        p = np.array([-self._l/2, -self._w/2, self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p6(self):
        p = np.array([self._l/2, -self._w/2, self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p7(self):
        p = np.array([self._l/2, self._w/2, self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p8(self):
        p = np.array([-self._l/2, self._w/2, self._h/2])
        p = self._q.rotate(p)
        p = p + self._c
        return np.append(p, 1)

    @property
    def p(self):
        x = np.vstack([self.p1, self.p2, self.p3, self.p4,
                       self.p5, self.p6, self.p7, self.p8])
        return x