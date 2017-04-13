key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
 
def decoder_encoder(inputString):
 
    newString = ""
 
    print(inputString)
 
    for word in (re.findall('[a-zA-Z0-9?!]+', inputString)):
        for j in range(len(word)):
            if word[j] in key:
                newString = newString+key[word[j]]
            else:
                newString = newString+word[j]
        newString = newString+" "
    print(newString)
             
 
decoder_encoder("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
 
print("\n")
 
decoder_encoder("Caesar cipher? I much prefer Caesar salad!")
