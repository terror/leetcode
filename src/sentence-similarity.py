class Solution:
  def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    if len(sentence1) != len(sentence2): return False

    def is_sim(a, b):
      if a == b: return True
      return any(a == c and d == b or a == d and b == c for c, d in similarPairs)

    return all(is_sim(a, b) for a, b in zip(sentence1, sentence2))
