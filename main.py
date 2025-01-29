"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
	""" done. """
	for i, v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
		mylist....list to search
		key.......search key
		left......left index into list to search
		right.....right index into list to search

	Returns:
		index of key in mylist, or -1 if not present.
	"""
	### TODO
	midpoint_index = (left +
	                  right) // 2  #index of the middle element of the list
	midpoint_value = mylist[
	    midpoint_index]  #value of the middle element of the list

	if midpoint_value == key:  #first, check if the middle element is the key
		return midpoint_index		 #return its index if it is
	
	elif key < midpoint_value:   # if the key is in the left half of the list, make the 
		right = midpoint_index - 1 # right end 1 less than the midpoint 
	
	elif key > midpoint_value:   # if the key is in the right half of the list, make the
		left = midpoint_index + 1  # left end 1 more than the midpoint
	
	if left > right:  # if key is not found in the list, return -1
		return -1
	
	return _binary_search(mylist, key, left, right) # recursive call to the function to continue search
###

def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start = time.time()  # start time
	search_fn(mylist, key)  # run the search function
	end = time.time()  # end time
	return (end - start) * 1000  # return the time in milliseconds
	###


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	returnList = []  # create an empty list to store the results
	for n in sizes:
		nList = list(range(int(n)))  # Generate the list from 0 to n-1, convert n to int so range can be used
		linear_search_time = time_search(linear_search, nList, -1)  # time linear search
		binary_search_time = time_search(binary_search, nList, -1)  # time binary search
		returnList.append((int(n), linear_search_time, binary_search_time))  # Ensure n is an int, append tuple to returnList
	return returnList
	###


def print_results(results):
	""" done """
	print(
	    tabulate.tabulate(results,
	                      headers=['n', 'linear', 'binary'],
	                      floatfmt=".3f",
	                      tablefmt="github"))

print_results(compare_search())