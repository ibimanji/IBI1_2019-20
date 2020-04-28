# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:11:05 2020

@author: yly
"""


'''
enter a string with N data, split the data into N simple strings with a split(),
then use map()to maps it to int,
then adds all the data to the list data by list()
'''
data = list(map(int, input("Please input numbers to compute 24:(use ',' to divide them)\n").split(',')))


'''
evaluate N, N value is the length of the list data
'''
N = len(data)


'''
judge whether the input data meets the requirements of 1~23,
if not meet, re-input.
judge_data() is used to judge whether data meets the requirements of 0<data<24,
if meet, return True
if not meet, return False
'''
def judge_data(data):
	flag_data = True
	for i in range(0, N):
		if data[i] <= 0 or data[i] >= 24:
			flag_data = False
	return flag_data


'''
while loop：if judge_data(), return False，
output the prompt message and ask the user to input again
'''
while not judge_data(data):
	print("The input number must be intergers from 1 to 23")
	data = list(map(int, input("Please input numbers to compute 24:(use ',' to divide them)\n").split(',')))


'''
def recursion function to find the 24 points calculation method of the data in the array list,
the algorithm is as follows:
get24(length=N){
	if(N==2) that is, there are only two elements in the array, so for the two elements,
             repearedly apply the + - * /,
             judge whether the result can be 24 points,
             if can, output
	if(N!=2) that is, there are three or more elements in the array,
             select two numbers from them and merge them into a new number
             (the merge method can be + _ * /)
             add the new number and the remaining numbers into a new array to become an array of length N-1
             and call get24 function
}
'''
Recursion_times = 0
def get24(array):
	#global Recursion_times evaluates the recursion times, adding 1 for each call
	global Recursion_times
	Recursion_times += 1
	#find the length of the array
	array_length = len(array)
    #judge whether the number of elements is 2. follows is the situation 'equal to 2'
	if array_length == 2:
		#repearedly apply the + - * /, if ok returns True, otherwise returns False
		if array[0] + array[1] == 24:
			return True
		elif array[0] - array[1] or array[1] - array[0] == 24:
			return True
		elif array[0] * array[1] == 24:
			return True
		elif array[0] / array[1] or array[1] / array[0] == 24:
			return True
		else:
			return False
	#udge whether the number of elements is 2. follows is the situation 'not equal to 2'
	if not array_length == 2:
		#get the last two elements of the data array to merge
		last1 = data[-1]
		last2 = data[-2]
		#merge_set is used to represent all possible new numbers for last1 and last2 by+-*/
		merge_set = []
		#press the new number into the list merge_set
		merge_set.append(last1+last2)
		merge_set.append(last1-last2)
		merge_set.append(last2-last1)
		merge_set.append(last1*last2)
		merge_set.append(last1/last2)
		merge_set.append(last2/last1)
        #For each number in merge_set, merge it with the previous len(array)-2 elements of data into the new list new_data
		for item in merge_set:
			new_data = []
			#Press the first len(array)-2 elements of data into the list new_data
			for i in range(array_length-2):
				new_data.append(data[i])
			#press the numbers in merge_set into the list new_data       
			new_data.append(item)
			#Call get24() recursively to see if it satisfies. if so, return True; if not, return False
			if get24(new_data):
				return True
			else:
				return False

			
'''
use recursive function to judge whether the data meets the requirements of 24 points,
output the information
'''
if get24(data):
	print("Yes")
	print("Recursion times: ", Recursion_times)
else:
	print("No")
	print("Recursion times: ", Recursion_times)