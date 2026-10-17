import math, unittest, numpy as np
from golden4.geometry import *

class Golden4GeometryTests(unittest.TestCase):
    def setUp(self):
        self.parent=regular_triangle()
        self.kids=split_triangle(*self.parent,+1)

    def test_golden_parameter(self):
        self.assertAlmostEqual(T,(5+math.sqrt(5))/10,14)

    def test_four_equal_areas(self):
        A=polygon_area(np.array(self.parent))
        for k in self.kids:
            self.assertAlmostEqual(polygon_area(k),A/4,12)

    def test_three_scalenes_congruent(self):
        ss=[side_lengths(k) for k in self.kids[:3]]
        self.assertTrue(np.allclose(ss[0],ss[1],atol=1e-12))
        self.assertTrue(np.allclose(ss[1],ss[2],atol=1e-12))

    def test_central_is_equilateral(self):
        s=side_lengths(self.kids[3])
        self.assertTrue(max(s)-min(s)<1e-12)
        self.assertAlmostEqual(s[0],0.5,12)

    def test_scalene_lengths(self):
        expected=sorted([(math.sqrt(5)-1)/4, (1+math.sqrt(5))/4, 1.0])
        self.assertTrue(np.allclose(side_lengths(self.kids[0]),expected,atol=1e-12))

    def test_children_cover_parent_area(self):
        self.assertAlmostEqual(sum(polygon_area(k) for k in self.kids),
                               polygon_area(np.array(self.parent)),12)

    def test_handedness_is_mirror_metric(self):
        plus=split_triangle(*self.parent,+1)
        minus=split_triangle(*self.parent,-1)
        # Same multiset of child side-length signatures.
        a=sorted(tuple(round(x,12) for x in side_lengths(k)) for k in plus)
        b=sorted(tuple(round(x,12) for x in side_lengths(k)) for k in minus)
        self.assertEqual(a,b)

if __name__=="__main__":
    unittest.main()
