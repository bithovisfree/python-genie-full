
import random

def sentencegen():
  nouns = ("puppy", "car", "rabbit", "girl", "monkey")
  verbs = ("runs", "hits", "jumps", "drives", "barfs")
  adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "gently", "loyally", "primarily", "roughly", "significantly")
  adj = ("Adorable", "Clueless", "Dirty", "Odd", "Stupid", "Huge", "Cuddly", "Sudden", "Chivalrous", "Slimy", "Perfect", "Normal", "Smart")
  num = random.randrange(0, 5)
  print(nouns[num] + ' ' + verbs[num] + ' ' + adj[num] + ' ' + adv[num])

sentencegen()
