text = """
Poe, E. 
Near a Raven 

Midnights so dreary, tired and weary, 
Silently pondering volumes extolling all by-now obsolete lore. 
During my rather long nap - the weirdest tap! 
An ominous vibrating sound disturbing my chamber's antedoor. 
"This", I whispered quietly, "I ignore."
"""

punct = [',', '-', '.', '"', '!', "'"]

words = text.split(' ')
lengths = []

for word in words:
  index = words.index(word)
  words[index] = word.strip()

  for mark in punct:
    words[index] = words[index].replace(mark, '')

  lengths.append(len(words[index]))

print lengths