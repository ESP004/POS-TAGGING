from typing import TypeAlias

Token : TypeAlias = str
TaggedToken : TypeAlias = tuple[str, str]
TaggedSentences :  TypeAlias = list[TaggedToken]