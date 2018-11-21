#!/ u s r / bin / env python
”””mapper . py ”””
import s y s
# i n p u t comes from STDIN ( s t and a rd i n p u t )
f o r l i n e i n s y s . s t di n :
# remove l e a di n g and t r a i l i n g whi te s p ace
l i n e = l i n e . s t r i p ( )
# s p l i t the l i n e i n t o words
words = l i n e . s p l i t ( )
# i n c r e a s e c o u n t e r s
f o r word i n words :
# w ri t e the r e s u l t s t o STDOUT ( s t and a rd output ) ;
# what we output h e r e w i l l be the i n p u t f o r the
# Reduce s tep , i . e . the i n p u t f o r r e d u c e r . py
#
# tab−d elimi t e d ; the t r i v i a l word count i s 1
p r i n t ’% s \ t%s ’ % ( word , 1 )
