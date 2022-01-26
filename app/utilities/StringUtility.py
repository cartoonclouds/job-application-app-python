

class StringUtility:
  
    @staticmethod
    def convertUpperToUnderscore(string: str) -> str:
      return ''.join('_' + char.lower() if char.isupper() else char
              for char in string).lstrip('_')