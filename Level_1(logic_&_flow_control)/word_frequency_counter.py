paragraph=''' a brief narrative with a beginning, middle, and end, often conveying a moral lesson. An example is the story of the crow and the fox: a crow with a piece of meat was praised by a fox who wanted it. The fox asked the crow to sing, and when the crow opened its mouth to caw, the meat fell out, and the fox ate it. '''
words=paragraph.split()
print(words)
w_count={}
for word in words:
    w_count[word]=words.count(word)
print(w_count)