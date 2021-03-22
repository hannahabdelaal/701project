from pyarabic.araby import strip_tashkeel

if __name__ == '__main__':
  text = u"الْعَرَبِيّةُ"
  print(strip_tashkeel(text))