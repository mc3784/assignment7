import numpy as np

#def generateAnswer():
print "#1 question"
startingArray=np.transpose(np.arange(1,16).reshape(3,5))

secondAndForthRows=np.concatenate((startingArray[1:2], startingArray[3:4]), axis=0)
print "Array containing 2nd and 4th rows:"
print secondAndForthRows

secondColumn=startingArray[:,1:2]
print "Array containing the second column:"
print secondColumn

threeMiddleRows=startingArray[1:4,:]
print "Array with all the elements in the rectangular section between the coordinates [1,0] and [3,2]:"
print threeMiddleRows
