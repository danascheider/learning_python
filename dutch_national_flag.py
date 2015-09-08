# This is from Edsger Dijkstra's book, "A Discipline of Programming".
#
# Imagine a board with a row of holes filled by red, white, and blue pegs. 
# Develop an algorithm which will swap pegs to make three bands of red, white,
# and blue (like the Dutch flag). You must also satisfy this additional
# constraint: each peg must be examined exactly once.
#
# Without the additional constraint, this is a relatively simple sorting
# problem. The additional constraint requires that instead of a simple sort, 
# which passes over the data several times, we need a more clever sort.
#
# Hint: You will need four partitions in the array. Initially, every peg is in
# the 'Unknown' partition. the other three partitions, 'Red', 'White', and
# 'Blue', are empty. When you are done, the 'Unknown' partition is reduced to
# zero elements, and the other three partitions have known numbers of elements. 