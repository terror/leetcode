class Solution:
  def romanToInt(self, s: str) -> int:
    table = {
      'I': 1,
      'IV': 4,
      'V': 5,
      'IX': 9,
      'X': 10,
      'XL': 40,
      'L': 50,
      'XC': 90,
      'C': 100,
      'CD': 400,
      'D': 500,
      'CM': 900,
      'M': 1000
    }

    i = 0
    tokens = []
    while i < len(s):
      if i + 1 < len(s):
        t = s[i] + s[i + 1]
        if t in ['XC', 'XL', 'CD', 'CM', 'IV', 'IX']:
          tokens.append(t)
          i += 2
          continue
      tokens.append(s[i])
      i += 1

    return sum(list(map(lambda token: table[token], tokens)))
