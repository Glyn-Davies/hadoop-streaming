#!/ u s r / bin / env python
”””mapper.py ”””
import sys
# i n p u t comes from STDIN ( s t and a rd i n p u t )
for line in sys.stdin:
# remove l e a di n g and t r a i l i n g whi te s p ace
line = line . strip( )
# s p l i t the l i n e i n t o words
words = line.split()
# i n c r e a s e c o u n t e r s
for word in words :
# w ri t e the r e s u l t s t o STDOUT ( s t and a rd output ) ;
# what we output h e r e w i l l be the i n p u t f o r the
# Reduce s tep , i . e . the i n p u t f o r r e d u c e r . py
#
# tab−d elimi t e d ; the t r i v i a l word count i s 1
print ’%s\t%s’ % (word, 1)
