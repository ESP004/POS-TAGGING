from core.nltk_data_types import Token

from nltk.tokenize import word_tokenize

class Tokenizer:
    """
    Responsible only for splitting text into tokens.

    Later we'll replace the implementation with NLTK.
    """

    def tokenize(self, text) -> list[Token]:
        
        if not text.strip():
            return []
        
        # tokenizer
        return word_tokenize(text)