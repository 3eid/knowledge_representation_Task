# knowledge representations Task
# Questions one & two
# Student name: Mohamed Eid Ali Gad
# Accademic number: 1900366


from utils import *
from logic2 import *

# Q1.1
#color(carrots, orange)
# carrots color is orange

carrots = Symbol('carrots')
orange = Symbol('orange')
knowledge1_1 = And(Implication(carrots, orange))

#output
#print(knowledge1_1.formula())

#########################################


# Q1.2
# likes(Person, carrots):-vegetarian(Person).
# if person is vegetarian , then person likes carrots "

person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like_carrots = Symbol("like(x, carrots)")
knowledge2_2 = And(Implication(vegetarian, like_carrots))

#output
#print(knowledge2_2.formula())

#########################################

# Q1.3
#pass(Student) :- study_hard(Student)
# student pass if he studies hard 
passes = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge1_3 = Implication(study_hard, passes)

#output
#print(knowledge1_3.formula())

#########################################

# Q1.4
# ?- pass(Who)
# who will pass?

Pass = Symbol("? pass(who)")
knowledge1_4 = And(Pass)

#output
#print(knowledge1_4.formula())

#########################################
# Q1.5
# ?- teaches(professor, Course)
# which course teacher teach ?
teaches = Symbol("? teaches(course, which)")
knowledge1_5 = And(teaches)

#output
#print(knowledge1_5.formula())

########################################

# Q 1.6
#enemies(X, Y) :- hates(X, Y), fights(X, Y)
#if (x & y are enemies), x hate y and x fight y

x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge1_6 = And(Implication(enemies, And(hates, fight)))

#output
#print(knowledge1_6.formula())



############################################################
#################### ----- Q2 ----- ########################

# Q2.1
#Maria reads logic programming book by author peter lucas.
# read(maria, logic programming book) --> by(peter lucas)
maria = Symbol("Maria")
peter_lucas = Symbol("Peter Lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge1_1 = And(Implication(read, by))

#output
# print(knowledge1_1.formula())

############################################################

# Q2.2
#Anyone likes shopping if she is a girl.
# is_girl(x) --> like(x, shopping)
isGirl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
Like = Symbol(f"like(x, {shopping} )")
knowledge2_2 = And(Implication(isGirl, Like))

#output
# print(knowledge2_2.formula())

############################################################
# Q2.3
#Who likes shopping?
# ? likes( x , shopping)

who = Symbol("?")
knowledge2_3  = And(who ,Like)

#output
# print(knowledge2_3.formula())

###########################################################

# Q2.4
#kirke hates any city if it is big and crowdy
# city( x ,big , crowdy) --> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge2_4 = And(Implication(city, hates))

#output
# print(knowledge2_4.formula())
