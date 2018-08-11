orginal=input ("Enter the new sentence")
#split in word
words=orginal.split();
#print(w)

#loop through words to convert in piglatin
#if strat with vowel add "yay"
new_words=[]

for word in words:
    #print(wordd)
    if word[0] in "aeiou":
        new_word= word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
                
            else:
                   break;
            cons=word[:vowel_pos]
            #print(cons)
            the_rest=word[vowel_pos:]
            #print(the_rest)
            new_word=the_rest+cons +"ay"
            new_words.append(new_word)
#print(new_words)


#stick words together 
output="  ".join(new_words)
print(output)
        


        

