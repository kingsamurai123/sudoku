def validate(arr , n):
	flag = 0
	for i in range(n):
		for j in range(n):
			ans = arr[i][j]
			if ans > 10:
				print("Invalid number")
				flag = 1
				break
			else:
				for ii in range(n):
					if ( j != ii and ans == arr[i][ii] ) or ( i != ii and ans == arr[ii][j]):
						flag = 1
						break
	if flag == 1:
		print("FAILED")
	else:
		print("GRAND SUCCESS")

def create_array(n , array):
	for i in range(n):
		temp = []
		for j in range(n):
			temp.append(int(input()))
		array.append(a)
	return array			

n = 9
array = []

example = [
[9,7,1,2,3,8,4,5,6],
[5,2,3,7,4,6,8,1,9],
[4,6,8,1,5,9,3,7,2],
[1,3,5,4,6,7,9,2,8],
[6,4,7,8,9,2,5,3,1],
[8,9,2,3,1,5,7,6,4],
[2,5,4,6,8,3,1,9,7],
[7,8,9,5,2,1,6,4,3],
[3,1,6,9,7,4,2,8,5]
]

example2 = [
[1,6,5,8,4,7,9,2,3],
[7,8,9,3,1,2,5,4,6],
[4,3,2,5,9,6,1,7,8],
[2,9,7,4,6,3,8,5,1],
[5,1,8,7,2,9,3,6,4],
[3,4,6,1,5,8,2,9,7],
[9,7,3,2,8,4,6,1,5],
[8,2,1,6,7,5,4,3,9],
[6,5,4,9,3,1,7,8,2]
]

# question = create_array( n , array )
validate( example2 , n )
