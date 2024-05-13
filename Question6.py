def delete_elements(array):
	# Declaring array and index to delete
	array = [3,7,1,9,4]
	print("Array before deletion:")
	print(array)
	i=array.index
	for i in array:
		if i<0 or i>=array.length:
			print ('Invalid index')
		
		return array.remove(i)
arr = [3,7,1,9,4]
print (delete_elements(arr))
			
	