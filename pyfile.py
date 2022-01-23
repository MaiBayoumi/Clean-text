import string 
import numpy as np
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

book1 = open("book1.txt", "r",encoding='utf-8')
text1 = book1.read()
book1.close()
words1 = text1.split() 
words1 = [word.lower() for word in words1] 
table1 = str.maketrans('', '', string.punctuation)
stripped1 = [w.translate(table1) for w in words1]
symbols1 = [word for word in stripped1 if word.isalpha()]
stop_words1 = set(stopwords.words('english'))
array1 = [w for w in symbols1 if not w in stop_words1]

book2=open("book2.txt","r",encoding='utf-8')
text2 = book2.read()
book2.close()
words2 = text2.split() 
words2 = [word.lower() for word in words2] 
table2 = str.maketrans('', '', string.punctuation) 
stripped2 = [w.translate(table2) for w in words2]
symbols2 = [word for word in stripped2 if word.isalpha()]
stop_words2 = stopwords.words('english')
array2 = [w for w in symbols2  if not w in stop_words2]

x = set (np.intersect1d(array1, array2))
print(x)
print(len(x))