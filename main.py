from pyarabic.araby import strip_tashkeel
from pyarabic.araby import strip_harakat

if __name__ == '__main__':
  text = u"الْعَرَبِيّةُ"
  print(strip_harakat(text))
  text = u"الْعَرَبِيّةُ"
  print(strip_tashkeel(text))