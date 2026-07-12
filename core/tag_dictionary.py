"""
Penn Treebank POS Tag Dictionary

Maps POS tags returned by NLTK to human-readable descriptions.
"""

TAG_MEANINGS = {
    # Coordinating conjunction
    "CC": "Coordinating Conjunction",

    # Numbers
    "CD": "Cardinal Number",

    # Determiners
    "DT": "Determiner",

    # Existential
    "EX": "Existential There",

    # Foreign word
    "FW": "Foreign Word",

    # Prepositions
    "IN": "Preposition / Subordinating Conjunction",

    # Adjectives
    "JJ": "Adjective",
    "JJR": "Comparative Adjective",
    "JJS": "Superlative Adjective",

    # List marker
    "LS": "List Item Marker",

    # Modal
    "MD": "Modal Verb",

    # Nouns
    "NN": "Noun (Singular)",
    "NNS": "Noun (Plural)",
    "NNP": "Proper Noun (Singular)",
    "NNPS": "Proper Noun (Plural)",

    # Predeterminer
    "PDT": "Predeterminer",

    # Possessive ending
    "POS": "Possessive Ending",

    # Pronouns
    "PRP": "Personal Pronoun",
    "PRP$": "Possessive Pronoun",

    # Adverbs
    "RB": "Adverb",
    "RBR": "Comparative Adverb",
    "RBS": "Superlative Adverb",

    # Particle
    "RP": "Particle",

    # Symbol
    "SYM": "Symbol",

    # "to"
    "TO": "to",

    # Interjection
    "UH": "Interjection",

    # Verbs
    "VB": "Verb (Base Form)",
    "VBD": "Verb (Past Tense)",
    "VBG": "Verb (Gerund /Present Participle)",
    "VBN": "Verb (Past Participle)",
    "VBP": "Verb (Non-3rd Person Singular Present)",
    "VBZ": "Verb (3rd Person Singular Present)",

    # Wh words
    "WDT": "Wh-Determiner",
    "WP": "Wh-Pronoun",
    "WP$": "Possessive Wh-Pronoun",
    "WRB": "Wh-Adverb",

    # Punctuation
    ".": "Sentence Terminator",
    ",": "Comma",
    ":": "Colon / Ellipsis",
    "(": "Opening Parenthesis",
    ")": "Closing Parenthesis",
    "\"": "Quotation Mark",
    "#": "Hash Symbol",
    "$": "Dollar Sign",
}


def get_tag_meaning(tag: str) -> str:
    """
    Returns a human-readable description of a POS tag.
    """

    return TAG_MEANINGS.get(tag, "Unknown POS Tag")