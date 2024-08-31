from pandocfilters import toJSONFilter, Emph, Para

def example(key, value, format, meta):
  print(f"{key} {value}")

if __name__ == "__main__":
  toJSONFilter(example)