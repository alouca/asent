from typing import Callable, Dict
import catalogue

import os
import codecs
from inspect import getsourcefile

lexicons = catalogue.create("asent", "lexicon", entry_points=True)
components = catalogue.create("asent", "components", entry_points=True)


def register_lexicon(name: str, lexicon: Dict[str, float]) -> None:
    """Registers a lexicon in asent.lexicons

    Args:
        name (str): The name of the lexicon
        lexicon (Dict[str, float]): The lexicon supplies as a dictionary.

    Example:
        >>> asent.register("my_lexicon_v1", {"happy": 4, "sad": -2})
        >>> asent.lexicons.get("my_lexicon_v1")
        {"happy": 4, "sad": -2}
    """
    lexicons.register(name, func=lexicon)


def register_component(name: str, func: Callable) -> None:
    """Registers a component in asent.components

    Args:
        name (str): The name of the lexicon
        func (Callable): A Callable component
    """
    components.register(name, func=func)

def read_lexicon(path: str) -> Dict[str, float]:

    _this_module_file_path_ = os.path.abspath(getsourcefile(lambda: 0))
    lexicon_full_filepath = os.path.join(
        os.path.dirname(_this_module_file_path_), path
    )
    with codecs.open(lexicon_full_filepath, encoding="utf-8") as f:
        lexicon = {}
        for line in f.read().rstrip("\n").split("\n"):
            if not line:
                continue
            (word, measure) = line.strip().split("\t")[0:2]
            lexicon[word] = float(measure)
    return lexicon
