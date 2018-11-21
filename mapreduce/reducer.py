#!/ u s r / bin / env python
””” r e d u c e r . py ”””
from o p e r a t o r import i t em g e t t e r
import s y s
c u r r e n t w o r d = None
c u r r e n t c o u n t = 0
word = None
# i n p u t comes from STDIN
f o r l i n e i n s y s . s t di n :
# remove l e a di n g and t r a i l i n g w hi t e s p a c e
l i n e = l i n e . s t r i p ( )
# p a r s e the i n p u t we g o t from mapper . py
word , count = l i n e . s p l i t ( ’ \ t ’ , 1 )
# c o n v e r t count ( c u r r e n t l y a s t r i n g ) t o i n t
t r y :
count = i n t ( count )
e x c e p t V alueE r r o r :
# count was not a number , s o s i l e n t l y
# i g n o r e / di s c a r d t h i s l i n e
c o n ti n u e
# t h i s IF−swi t c h onl y works bec au se Hadoop s o r t s map output
# by key ( h e r e : word ) b e f o r e i t i s p a s sed t o the r e d u c e r
i f c u r r e n t w o r d == word :
c u r r e n t c o u n t += count
e l s e :
i f c u r r e n t w o r d :
# w ri t e r e s u l t t o STDOUT
p r i n t ’% s \ t%s ’ % ( cu r ren t w o rd , c u r r e n t c o u n t )
c u r r e n t c o u n t = count
c u r r e n t w o r d = word
i f c u r r e n t w o r d == word :
p r i n t ’% s \ t%s ’ % ( cu r ren t w o rd , c u r r e n t c o u n t )
