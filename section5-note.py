from copy import deepcopy

## List
listA = list([1,2,3,4])
listB = [1,2,3,4]

# This code make error of index out of range
# listA[4] = 5

# print('listA', listA,listA[-1], len(listA), type(listA))

## -------------------------------------------------------------------------------------
## Tuple
tupleA = tuple([1, 'a', True, [2,3]])
tupleB = (1,'a', True, [2,3])
tupleC = 1, 'a', True, [2,3]

tupleAA = tupleA[-1]

tupleAA[-1] = 5

a = 10
b =20
tupleD = a, b, a+b

listOfTupleB = list(tupleB)
listOfTupleB[-1][-1] = 9

list2OfTupleB = list(tupleB)
list2OfTupleB[0] = 0

# print('tupleAA', tupleAA, type(tupleAA))
# print('tupleA', tupleA, type(tupleA))
# print('tupleB', tupleB, type(tupleB))
# print('listOfTupleB', listOfTupleB, type(listOfTupleB))
# print('list2OfTupleB', list2OfTupleB, type(list2OfTupleB))
# print('tupleC', tupleC, type(tupleC))
# print('tupleD', tupleD, type(tupleD))

## -------------------------------------------------------------------------------------
## String
strA = 'Python\'best features'

# print('strA', strA, type(strA))

## -------------------------------------------------------------------------------------
## Manipulating
listC = [1,2,3,4,5]
listC[0:3] = ['a','b']
del listC[0]
listC.extend([6,7,8])
listC.extend((9,10))
listC.extend('cde')

# print('listC', listC, type(listC))

## -------------------------------------------------------------------------------------
## Shallow & deep copying sequences
listD = [[1,2],'a','b']
copyOfListD = listD.copy()
copyOfListD[1] = 'c'

listE = [[1,(2,3)],1,'b']
copyOfListE = deepcopy(listE)

listF = [1,2,3]
copyOfListF = listF[:]
copyOfListF.append(4)

# print('compare listD and copyOfListD',copyOfListD[1] is listD[1])
# print('listD', listD, type(listD))
# print('copyOfListD', copyOfListD, type(copyOfListD))
# print('listF', listF, type(listF))
# print('copyOfListF', copyOfListF, type(copyOfListF))
# print('compare listE and copyOfListE',copyOfListE[0][1] is listE[0][1])
# print('listE', listE, type(listE))
# print('copyOfListE', copyOfListE, type(copyOfListE))

## -------------------------------------------------------------------------------------
## Unpacking sequence
listG = [1,2,3]

a,b,c = listG

a,b=b,a

# print('a', a)
# print('b', b)
# print('c', c)
