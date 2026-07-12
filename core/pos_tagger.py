import nltk

from core.nltk_data_types import TaggedToken

class PosTagger:
    """
    Responsible only for assigning POS tags.

    Current implementation is temporary.
    Later it will use NLTK.
    """

    def tag(self, tokens: list[str]) -> list[TaggedToken]:
        
        return nltk.pos_tag(tokens)