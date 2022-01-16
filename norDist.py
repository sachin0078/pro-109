import csv
import statistics
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")

score=df["math score"].to_list()

score_mean=statistics.mean(score)
score_median=statistics.median(score)
score_mode=statistics.mode(score)

score_stdev=statistics.stdev(score)

print("mean of the math score:" ,score_mean)
print("median of the math score:" ,score_median)
print("mode of the math score:" ,score_mode)
print("standard deviation of the math score" ,score_stdev)

first_std_dev_start,first_std_dev_end=score_mean-score_stdev, score_mean+score_stdev
second_std_dev_start,second_std_dev_end=score_mean-(2*score_stdev), score_mean+(2*score_stdev)
third_std_dev_start,third_std_dev_end=score_mean-(3*score_stdev), score_mean+(3*score_stdev)

data_within_1_std_deviation=[result for result in score if result > first_std_dev_start and result < first_std_dev_end]
data_within_2_std_deviation=[result for result in score if result > second_std_dev_start and result < second_std_dev_end]
data_within_3_std_deviation=[result for result in score if result > third_std_dev_start and result < third_std_dev_end]

print("{} % of data for score lies within 1st std".format(len(data_within_1_std_deviation)*100.0/len(score)))
print("{} % of data for score lies within 2nd std".format(len(data_within_2_std_deviation)*100.0/len(score)))
print("{} % of data for score lies within 3rd std".format(len(data_within_3_std_deviation)*100.0/len(score)))


