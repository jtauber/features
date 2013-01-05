#!/usr/bin/env python3

from collections import defaultdict


# define some segments per Dresher chp.2 (2)

p = dict(name="p", voiced=False, nasal=False)
b = dict(name="b", voiced=True, nasal=False)
m = dict(name="m", voiced=True, nasal=True)


def pairwise_algorithm(segments):
    """
    pairwise algorithm for finding contrastive features for the given segments.
    
    based on (4) in Dresher chp.2
    """
    
    segment_pairs = [(x, y) for x in segments for y in segments if x["name"] < y["name"]]
    
    # key is a segment name, value is a set of those features that are contrastive
    # for that segment
    contrastive_features = defaultdict(set)
    
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
        if contrastive_feature:
            contrastive_features[x["name"]].add(contrastive_feature)
            contrastive_features[y["name"]].add(contrastive_feature)
    
    return contrastive_features


print(pairwise_algorithm([p, b, m]))
