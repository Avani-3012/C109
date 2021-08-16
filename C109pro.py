import random
import plotly.figure_factory as ff
import pandas
import statistics
 
file1 = pandas.read_csv('StudentsPerformance.csv')
maths =file1['math score'].tolist()
fig = ff.create_distplot([maths],['Math Score Chart'],show_hist=False)
fig.show()
mean = statistics.mean(maths)
print(mean)
median =  statistics.median(maths)
print(median)
standardDeviation = statistics.stdev(maths)
print(standardDeviation)



firstStandardDev_start,firstStandardDev_end, = mean-standardDeviation,mean+standardDeviation
secStandardDev_start,secStandardDev_end = mean-(2*standardDeviation),mean+(2*standardDeviation)
thirdStandardDev_start,thirdStandardDev_end = mean-(3*standardDeviation),mean+(3*standardDeviation)

thin1standardDev =[result for result in maths if result>firstStandardDev_start and result<firstStandardDev_end]
thin2standardDev =[result for result in maths if result>secStandardDev_start and result<secStandardDev_end]
thin3standardDev =[result for result in maths if result>thirdStandardDev_start and result<thirdStandardDev_end]
print("{}  of data for height lies within standard deviation".format(len(thin1standardDev)*100.0/len(maths)))
print("{} of data for height lies within standard deviation".format(len(thin2standardDev)*100.0/len(maths)))
print("{} of data for height lies within standard deviation".format(len(thin3standardDev)*100.0/len(maths)))