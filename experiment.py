#!/usr/bin/env python3

from collections import defaultdict
import pprint

# define some segments per Dresher chp.2 (2)

p = dict(name="p", voiced=False, nasal=False)
b = dict(name="b", voiced=True, nasal=False)
m = dict(name="m", voiced=True, nasal=True)

segments_by_name = {segment["name"]: segment for segment in [p, b, m]}


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

pp = pprint.PrettyPrinter(indent=2)


pp.pprint(pairwise_algorithm([p, b, m]))


def partition(segments, feature):
    values = defaultdict(set)
    for segment in segments:
        assert feature in segment
        values[segment[feature]].add(segment["name"])
    return values


def successive_division_algorithm(segments, feature_order):
    """
    successive division algorithm for finding the contrastive feature tree for
    the given segments assuming the given feature order.
    
    based on (9) and fn3 in Dresher chp.2
    """
    if not feature_order:
        assert len(segments) == 1
        return segments[0]["name"]
    p = partition(segments, feature_order[0])
    if len(p) == 1:
        assert len(segments) == 1
        return segments[0]["name"]
    d = {}
    for k, v in p.items():
        d[(feature_order[0], k)] = successive_division_algorithm([segments_by_name[name] for name in v], feature_order[1:])
    return d

d = successive_division_algorithm([p, b, m], ["nasal", "voiced"])
pp.pprint(d)

d = successive_division_algorithm([p, b, m], ["voiced", "nasal"])
pp.pprint(d)


# example from (19)

i = dict(name="i", high=True, low=False, back=False, round=False)
e = dict(name="e", high=False, low=False, back=False, round=False)
a = dict(name="a", high=False, low=True, back=True, round=False)
o = dict(name="o", high=False, low=False, back=True, round=True)
u = dict(name="u", high=True, low=False, back=True, round=True)

pp.pprint(pairwise_algorithm([i, e, a, o, u]))

# example from (20)

i = dict(name="i", high=True, round=False)
a = dict(name="a", high=False, round=False)
u = dict(name="u", high=True, round=True)

pp.pprint(pairwise_algorithm([i, a, u]))

# example from (21)

i = dict(name="i", high=True, back=False, round=False)
a = dict(name="a", high=False, back=True, round=False)
u = dict(name="u", high=True, back=True, round=True)

pp.pprint(pairwise_algorithm([i, a, u]))
