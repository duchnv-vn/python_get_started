## List
listA = list([1,2,3,4])
listB = [1,2,3,4]

# This code make error of index out of range
# listA[4] = 5

# print('listA', listA,listA[-1], len(listA), type(listA))

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
print('tupleD', tupleD, type(tupleD))

## String
strA = 'Python\'best features'
strOfTupleD = str(tupleD)
tupleOfStrOfTupleD = tuple(strOfTupleD)

# print('strA', strA, type(strA))
print('strOfTupleD', strOfTupleD, type(strOfTupleD))
print('tupleOfStrOfTupleD', tupleOfStrOfTupleD, type(tupleOfStrOfTupleD))