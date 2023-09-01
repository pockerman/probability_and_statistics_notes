"""Various utilities for the probability notes

"""
from typing import Union, Set, Dict, Callable


def get_events(event_condition: Callable, sample_space: Union[Set, Dict]):
    """Given the boolean callable event_condition returns the
    events from the sample space that satisfy it.

    Parameters
    ----------
    event_condition: A boolean callable
    sample_space: The sample space to use. This can either be
    a set or a dictionary where the keys are the outcomes and the
    values the weights. So fair coin can be modelled as
    sample_space = {'H': 1, 'T': 1}  whilst a biased coin that
    is four times more likely to get heads than tails the sample space is
    sample_space = {'H': 4, 'T': 1}

    Returns
    -------

    """
    return set([outcome for outcome in sample_space
                if event_condition(outcome)])