#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.colorimetry.illuminants` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.colorimetry import (D_illuminant_relative_spd,
                                CIE_standard_illuminant_A_function,
                                SpectralPowerDistribution)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2017 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'D60_SPD_DATA', 'A_DATA', 'TestD_illuminantRelativeSpd',
    'TestCIEStandardIlluminantAFunction'
]

D60_SPD_DATA = {
    300: 0.029370758174923,
    310: 2.619241317964963,
    320: 15.716890613128260,
    330: 28.774580263919134,
    340: 31.864839936661980,
    350: 36.377426444674100,
    360: 38.683115463162864,
    370: 42.717548461834966,
    380: 41.454940579637523,
    390: 46.605319243279432,
    400: 72.278593838848636,
    410: 80.440599992794645,
    420: 82.915026938943186,
    430: 77.676263977317561,
    440: 95.681274303793984,
    450: 107.954820867505958,
    460: 109.559186805074063,
    470: 107.758140706827916,
    480: 109.671404235341797,
    490: 103.707873310050914,
    500: 105.232198575232047,
    510: 104.427666921854353,
    520: 102.522933578052459,
    530: 106.052670879047824,
    540: 103.315154034581980,
    550: 103.538598917326581,
    560: 100.000000000000000,
    570: 96.751421418866897,
    580: 96.712822501540316,
    590: 89.921479084426167,
    600: 91.999793295044071,
    610: 92.098709550672751,
    620: 90.646002697010346,
    630: 86.526482724860287,
    640: 87.579186235501524,
    650: 83.976140035832955,
    660: 84.724074228057717,
    670: 87.493490847729831,
    680: 83.483070156949736,
    690: 74.172451118766631,
    700: 76.620385310991381,
    710: 79.051849073755832,
    720: 65.471370717416463,
    730: 74.106079027252520,
    740: 79.527120427726302,
    750: 67.307162771623837,
    760: 49.273538206159095,
    770: 70.892412117890245,
    780: 67.163996226304974,
    790: 68.171370717416465,
    800: 62.989808616705801,
    810: 54.990892361077115,
    820: 60.825600670913168,
    830: 63.893495862261560
}

A_DATA = np.array([
    6.144617784123856,
    6.947198985402079,
    7.821349414981689,
    8.769802283876084,
    9.795099608867382,
    10.899576157801631,
    12.085345363411140,
    13.354287257777719,
    14.708038449875502,
    16.147984141480254,
    17.675252152303049,
    19.290708903610355,
    20.994957290865997,
    22.788336360042955,
    24.670922689127945,
    26.642533365850888,
    28.702730444663004,
    30.850826760279453,
    33.085892971502503,
    35.406765707340028,
    37.812056687427500,
    40.300162690239553,
    42.869276245337296,
    45.517396929746482,
    48.242343153313406,
    51.041764323370195,
    53.913153285099291,
    56.853858940467404,
    59.861098955389089,
    62.931972471732792,
    66.063472747830630,
    69.252499658171686,
    72.495871989904842,
    75.790339480551324,
    79.132594547909648,
    82.519283669449450,
    85.947018374529335,
    89.412385818490364,
    92.911958913061213,
    96.442305992552875,
    100.000000000000000,
    103.581627181740913,
    107.183795282900803,
    110.803141239869944,
    114.436338369157482,
    118.080103054962819,
    121.731200940444666,
    125.386452630022220,
    129.042738912085099,
    132.697005513293647,
    136.346267397171545,
    139.987612621004047,
    143.618205766130785,
    147.235290957601734,
    150.836194489858400,
    154.418327075631083,
    157.979185735603039,
    161.516355346632452,
    165.027509866420871,
    168.510413252511256,
    171.962920093394303,
    175.382975969299480,
    178.768617559985131,
    182.117972516492841,
    185.429259113445994,
    188.700785698018507,
    191.930949951225926,
    195.118237976664375,
    198.261223231287033,
    201.358565312239051,
    204.409008613197130,
    207.411380863071741,
    210.364591559332979,
    213.267630307635471,
    216.119565078810581,
    218.919540393725441,
    221.666775445909082,
    224.360562171292912,
    227.000263273843757,
    229.585310215328150,
    232.115201176917310,
    234.589498999828919,
    237.007829111703302,
    239.369877444937316,
    241.675388352737258,
    243.924162528208456,
    246.116054931382024,
    248.250972728666568,
    250.328873248841006,
    252.349761959321199,
    254.313690466103111,
    256.220754540440964,
    258.071092175015735,
    259.864881672054366,
])


class TestD_illuminantRelativeSpd(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.illuminants.D_illuminant_relative_spd`
    definition unit tests methods.
    """

    def test_D_illuminant_relative_spd(self):
        """
        Tests :func:`colour.colorimetry.illuminants.D_illuminant_relative_spd`
        definition.
        """

        spd_r = SpectralPowerDistribution(D60_SPD_DATA)
        spd_t = D_illuminant_relative_spd(np.array([0.32168, 0.33767]))

        np.testing.assert_array_equal(spd_r.domain, spd_t.domain)
        np.testing.assert_almost_equal(spd_r.values, spd_t.values, decimal=7)


class TestCIEStandardIlluminantAFunction(unittest.TestCase):
    """
    Defines :func:`colour.colorimetry.illuminants.\
CIE_standard_illuminant_A_function` definition unit tests methods.
    """

    def test_CIE_standard_illuminant_A_function(self):
        """
        Tests :func:`colour.colorimetry.illuminants.\
CIE_standard_illuminant_A_function` definition.
        """

        np.testing.assert_almost_equal(
            CIE_standard_illuminant_A_function(np.arange(360, 830, 5)),
            A_DATA,
            decimal=7)


if __name__ == '__main__':
    unittest.main()
