from collections import Counter
from core.pos_categories import POS_CATEGORIES

class GrammarAnalyzer:

    def analyze(self, tagged_tokens):

        counts = Counter()

        for _, tag in tagged_tokens:

            category = POS_CATEGORIES.get(tag)

            if category:
                counts[category] += 1

        counts["Total Words"] = len(tagged_tokens)

        return dict(counts)