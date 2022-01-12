class Solution:
  def intToRoman(self, num: int) -> str:
    table = {
      1000: 'M',
      900: 'CM',
      500: 'D',
      400: 'CD',
      100: 'C',
      90: 'XC',
      50: 'L',
      40: 'XL',
      10: 'X',
      9: 'IX',
      5: 'V',
      4: 'IV',
      1: 'I'
    }

    ret = ''
    for key in table:
      rem = num % key
      if num // key > 0:
        ret += (num // key) * table[key]
      num = rem
    return ret
