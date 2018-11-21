#!/ u s r / bin / env python
”””reducer.py”””
from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
# i n p u t comes from STDIN
for line in sys.stdin :
# remove l e a di n g and t r a i l i n g w hi t e s p a c e
line=line.strip( )
# p a r s e the i n p u t we g o t from mapper . py
word , count = line.split( ’\t’ , 1 )
# c o n v e r t count ( c u r r e n t l y a s t r i n g ) t o i n t
try:
count = int( count )
except ValueError :
# count was not a number , s o s i l e n t l y
# i g n o r e / di s c a r d t h i s l i n e
continue
# t h i s IF−swi t c h onl y works bec au se Hadoop s o r t s map output
# by key ( h e r e : word ) b e f o r e i t i s p a s sed t o the r e d u c e r
if current_word == word :
current_count += count
else :
if current_word :
# w ri t e r e s u l t t o STDOUT
print ’%s\t%s’ % (current_word , current_count)
current_count = count
current_word = word
if current_word == word :
print ’%s\t%s’ % (current_word , current_count)
