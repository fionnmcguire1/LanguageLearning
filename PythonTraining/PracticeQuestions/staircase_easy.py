'''
Author: Fionn Mcguire
Description: Observe that its base and height are both equal to ,
and the image is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.

Eg. Input = 5
Output = 
    #
   ##
  ###
 ####
#####
'''

height = int(input('How tall is the staircase? '))

#Using for loop
#O^n
#Space complexity = n
for i in range(1,height+1):
    print(((height-i)*' ')+('#'*i))
