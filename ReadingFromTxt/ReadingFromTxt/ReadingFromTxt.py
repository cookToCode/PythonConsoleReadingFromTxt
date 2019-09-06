#cookToCode 2/6/19 Midterm SE126.52

##LINE 40 NEEDS TO BE CHANGED TO RUN ON YOUR PC

#This program will take a .txt file and format the data into lists.
#This program will also convert data to floats and then average them and spit out the avg + the letter grade associated to that averaged number

#--------------variable dictionary-----------------

lastName=[]     #holds the place for the names of the students in the .txt
test1=[]        #holds the place for the grades of test1
test2=[]        #holds the place for the grades of test2
test3=[]        #holds the place for the grades of test3
test4=[]        #holds the place for the grades of test4
test5=[]        #holds the place for the grades of test5
totTest=0       #The value of test1-5 added for each student
avgGrade=0      #The average of test1-5
let='q'         #This is the letter grade associated with the average grade(avgGrade)
numRec=0        #holds the value of the number of records that the program reads
totAvg=0        #holds the value of all the average grades added together
classAvg=0      #holds the total average grade of the class
passing=0       #holds the number of students passing the class
failed=0        #holds the number of students failing the class

#--------------functions---------------------------
def letter(x):  #This function takes the average grade and spits out the corresponding letter grade
    if x>=90:
        let='A'
    elif x>=80:
        let='B'
    elif x>=70:
        let='C'
    elif x>=60:
        let='D'
    else:
        let='F'
    return let
#--------------program begins----------------------
import csv
with open("Z:\\Midterm\\midterm_.txt") as csvfile:
    file=csv.reader(csvfile)
    
    for rec in file:    #This for loop will assign the recs into their corresponding lists
        numRec +=1
        #print(rec)
        lastName.append(rec[0])
        test1.append(float(rec[1]))
        test2.append(float(rec[2]))
        test3.append(float(rec[3]))
        test4.append(float(rec[4]))
        test5.append(float(rec[5]))
    #print(numRec)
    
    #Now we are done using the csv file

for i in range(0,numRec):   #This loop takes the value in each list for the amount of values in each list
    totTest=test1[i]+test2[i]+test3[i]+test4[i]+test5[i]    #Adds the test grades for the same position in each list
    avgGrade=float(totTest/5)   #averages the grades
    let=letter(avgGrade)        #Function call that sends back the letter grade
    #This if/else will count the number of students passing or failing in the class
    if let=='F':
        failed+=1
    else:
        passing+=1
    totAvg+=avgGrade            #This holds the value of all the average grades added together for a class average
    print(f'{lastName[i]:8}{test1[i]:.0f}{test2[i]:6.0f}{test3[i]:6.0f}{test4[i]:6.0f}{test5[i]:6.0f}{avgGrade:8.2f} {let}')
classAvg=totAvg/numRec
let=letter(classAvg)
print(f'\nThe class average is {classAvg:.2f} {let}')
print(f'\nThere are {passing} students passing and {failed} students failing.\n\n')