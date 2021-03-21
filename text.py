def revword(word:str) -> str:
    word=list(word)
    new_word=[]

    for letter in reversed(word):
      
        new_word.append(letter.lower())
    
    new_word=''.join(new_word)
    
    return new_word


def countword()->int:
    file = open("text.txt", 'r' )
    text =file.read()
    file.close()
    text=text.split()
    word=text[0]
    new_text=[]
    for all_word in text[1:]:
        new_text.append(revword(all_word))     
    count=new_text.count(word)+1     

    return count
