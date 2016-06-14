#this creates an array and assignes it a value of zero
#similar to assigning a variable to zero (variable = 0)
array_score = [0]

result_f = open("results.txt")
for line in result_f:
    #this splits the lines of the file into two variables (name and score)
    #uses the "split()" function
    (name, score) = line.split()
    array_score.append(float(score))
result_f.close()

#by default the sort function is lowest-to-highest
#so we have to reverse the order
#could also used "array_score.sort(reverse=true)"
#this would have saved a line of code
array_score.sort()
array_score.reverse()

print("The top scores were: ")
print(array_score[0])
print(array_score[1])
print(array_score[2])


