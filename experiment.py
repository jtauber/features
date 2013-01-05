#!/usr/bin/env python3


# define some segments per Dresher chp.2 (2)

p = dict(name="p", voiced=False, nasal=False)
b = dict(name="b", voiced=True, nasal=False)
m = dict(name="m", voiced=True, nasal=True)

segments = [p, b, m]

# Pairwise Algorithm chp.2 (4)

segment_pairs = [(x, y) for x in segments for y in segments if x["name"] < y["name"]]

for x, y in segment_pairs:
    assert x.keys() == y.keys()
    contrastive_feature = None
    for k, v in x.items():
        if k != "name" and v != y[k]:
            if contrastive_feature is None:
                contrastive_feature = k
            else:
                contrastive_feature = None
                break
    print(x["name"], y["name"], contrastive_feature)

# @@@
