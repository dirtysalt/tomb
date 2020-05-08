#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def cmp_fn(x, y):
            w0, h0 = x
            w1, h1 = y
            if w0 == w1:
                return h1 - h0
            return w0 - w1

        import functools
        envelopes.sort(key=functools.cmp_to_key(cmp_fn))

        # print(envelopes)
        dp = []
        for w, h in envelopes:
            s, e = 0, len(dp) - 1
            while s <= e:
                m = (s + e) // 2
                if dp[m] >= h:
                    e = m - 1
                else:
                    s = m + 1
            if s == len(dp):
                dp.append(h)
            else:
                dp[s] = min(dp[s], h)

        # print(dp)
        ans = len(dp)
        return ans


cases = [
    ([], 0),
    ([[30, 50], [12, 2], [3, 4], [12, 15]], 3),
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ([[911, 339], [444, 378], [726, 608], [610, 758], [154, 643], [400, 428], [319, 221], [36, 68], [944, 863],
      [49, 779], [269, 640], [679, 772], [224, 754], [859, 593], [692, 814], [560, 442], [216, 510], [915, 822],
      [518, 740], [689, 522], [920, 264], [867, 976], [803, 969], [975, 719], [844, 463], [783, 25], [614, 185],
      [581, 51], [608, 973], [664, 712], [240, 943], [591, 403], [423, 211], [147, 436], [371, 873], [236, 45],
      [827, 746], [219, 882], [95, 775], [689, 691], [413, 222], [424, 947], [132, 738], [872, 712], [57, 147],
      [702, 556], [291, 675], [22, 657], [331, 411], [710, 11], [942, 816], [287, 631], [52, 121], [164, 531],
      [137, 660], [296, 763], [402, 982], [678, 408], [546, 216], [328, 911], [168, 914], [902, 811], [251, 992],
      [58, 852], [584, 158], [404, 284], [936, 212], [261, 714], [911, 71], [212, 33], [560, 85], [258, 672],
      [967, 292], [201, 698], [824, 732], [893, 706], [963, 509], [707, 921], [730, 722], [587, 19], [978, 584],
      [439, 694], [985, 340], [430, 14], [208, 123], [397, 504], [466, 244], [966, 323], [371, 282], [502, 572],
      [867, 488], [463, 96], [846, 48], [316, 986], [373, 559], [360, 885], [903, 280], [598, 789], [417, 467],
      [425, 438], [527, 737], [522, 265], [779, 648], [987, 435], [613, 751], [353, 690], [528, 229], [225, 699],
      [999, 69], [485, 802], [264, 115], [303, 635], [418, 759], [347, 925], [289, 764], [268, 430], [822, 219],
      [51, 939], [360, 289], [644, 140], [281, 399], [248, 90], [52, 850], [810, 164], [578, 398], [485, 835],
      [875, 803], [277, 347], [29, 139], [450, 358], [563, 943], [291, 423], [575, 475], [14, 162], [944, 46],
      [379, 962], [162, 673], [540, 239], [988, 204], [430, 535], [420, 500], [26, 68], [148, 860], [811, 920],
      [942, 305], [224, 806], [903, 131], [595, 591], [775, 524], [424, 732], [500, 189], [280, 121], [624, 521],
      [401, 30], [272, 494], [907, 476], [31, 344], [148, 335], [1, 353], [302, 532], [25, 388], [276, 2], [604, 109],
      [342, 537], [941, 203], [634, 914], [444, 99], [540, 505], [102, 811], [449, 32], [228, 980], [50, 498],
      [261, 454], [48, 24], [647, 553], [81, 768], [695, 554], [970, 465], [371, 908], [966, 447], [677, 796],
      [523, 752], [822, 190], [601, 920], [55, 364], [320, 121], [656, 357], [291, 321], [148, 615], [598, 798],
      [64, 588], [792, 982], [385, 530], [738, 694], [174, 789], [31, 23], [381, 562], [90, 368], [340, 966], [162, 70],
      [627, 296], [235, 662], [893, 585], [540, 819], [544, 107], [631, 927], [192, 581], [167, 379], [256, 86],
      [820, 819], [552, 404], [673, 936], [337, 391], [704, 792], [276, 788], [793, 640], [399, 140], [836, 809],
      [399, 726], [741, 14], [907, 270], [134, 578], [940, 568], [90, 585], [452, 761], [376, 157], [414, 860],
      [430, 773], [60, 547], [266, 350], [921, 278], [940, 845], [494, 978], [87, 538], [957, 989], [267, 162],
      [558, 164], [686, 848], [883, 872], [650, 414], [895, 227], [72, 833], [280, 44], [784, 789], [615, 512],
      [193, 471], [73, 40], [609, 184], [180, 157], [590, 635], [842, 335], [355, 388], [526, 347], [106, 828],
      [15, 154], [139, 588], [494, 437], [966, 606], [12, 56], [14, 203], [535, 844], [150, 896], [377, 369],
      [867, 624], [513, 568], [819, 484], [857, 793], [480, 664], [335, 657], [59, 238], [48, 537], [962, 925],
      [863, 277], [597, 111], [212, 476], [940, 418], [994, 438], [796, 195], [428, 179], [583, 717], [941, 913],
      [126, 971], [301, 2], [302, 766], [242, 771], [587, 301], [869, 721], [395, 411], [544, 741], [816, 480],
      [387, 190], [978, 376], [336, 781], [282, 716], [907, 52], [976, 114], [694, 924], [23, 358], [776, 866],
      [322, 744], [35, 708], [359, 339], [661, 433], [995, 697], [760, 154], [348, 446], [559, 319], [509, 631],
      [339, 441], [414, 705], [52, 939], [725, 319], [568, 235], [269, 143], [744, 505], [859, 305], [233, 746],
      [637, 269], [353, 249], [348, 275], [860, 501], [772, 492], [839, 747], [10, 351], [205, 350], [784, 245],
      [800, 199], [655, 343], [570, 307], [492, 842], [486, 795], [58, 887], [852, 408], [36, 626], [849, 134],
      [651, 268], [922, 592], [90, 333], [429, 503], [392, 579], [4, 593], [908, 203], [955, 346], [628, 749],
      [943, 910], [545, 784], [370, 946], [43, 614], [759, 816], [656, 508], [980, 375], [58, 863], [220, 612],
      [856, 290], [980, 302], [492, 408], [802, 875], [998, 867], [87, 571], [884, 318], [33, 632], [626, 343],
      [62, 957], [647, 701], [588, 616], [371, 697], [562, 118], [52, 51], [521, 510], [242, 992], [663, 113],
      [490, 371], [77, 114], [418, 39], [998, 83], [926, 390], [810, 326], [437, 589], [69, 288], [38, 36], [409, 665],
      [192, 467], [754, 367], [110, 273], [223, 55], [39, 401], [108, 260], [556, 173], [937, 764], [548, 773],
      [576, 576], [292, 430], [912, 245], [104, 729], [565, 43], [637, 645], [118, 438], [149, 453], [58, 39],
      [171, 356], [87, 298], [10, 663], [673, 138], [798, 572], [986, 395], [43, 37], [841, 367], [357, 474],
      [414, 315], [444, 302], [165, 120], [841, 417], [840, 993], [706, 315], [63, 520], [339, 390], [942, 877],
      [406, 593], [606, 202], [492, 58], [130, 644], [452, 534], [810, 792], [843, 705], [900, 642], [194, 302],
      [222, 415], [654, 793], [253, 966], [206, 997], [702, 730], [948, 861], [444, 788], [809, 457], [400, 646],
      [321, 64], [598, 627], [302, 222], [465, 455], [681, 994], [824, 975], [277, 310], [268, 121], [498, 622],
      [800, 657], [90, 715], [804, 34], [106, 3], [711, 960], [810, 16], [703, 499], [972, 271], [762, 992]], 40),
]

import aatest_helper

sol = Solution()
aatest_helper.run_test_cases(sol.maxEnvelopes, cases)
