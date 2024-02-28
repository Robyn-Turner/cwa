import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
import matplotlib.pyplot as plt

def interpret_mood(avg_mood):
    if avg_mood>=9:
        return"Excellent"
    elif avg_mood<5:
        return "Good yet can be improved"
    elif 5<= avg_mood<9:
        return"Needs a lot of work "
    else:
        return"not sure , not enough info \n"


#Take them in as integers, as all inputs default to strings
Opinion = int(input("On a scale of 1-10 how good are period tracking apps in your opinion"))
Time = int(input("How often do you use period tracking apps"))
Wellbeing = int(input("On a scale to 1-10 how do period tracking apps improve your wellbeing"))
avg_mood = round(mean([Opinion,Time,Wellbeing]),2)
mood_remark = interpret_mood(avg_mood)
print("My expierience with peroid tracking apps is  ",mood_remark, " ", avg_mood)

file_path = '7.csv'

with open(file_path, 'r', newline='') as csvfile:
 
    csv_reader = csv.reader(csvfile)
    
    
    for row in csv_reader:
        
        print(row)  

data = pd.read_csv('7.csv')


plt.figure(figsize=(8, 6))
plt.pie( labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Categories')
plt.show()













#df = pd.read_csv('105657.csv')
#print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
#light_min = df['Light'].min()
#light_max = df['Light'].max()
#light_mean = df['Light'].mean()
#print (light_min,light_max,light_mean, avg_mood)

#f=open("BR1-3_results.csv","a",newline='')
#csver=cvs.writer(f)
#csver.writerow([light_min,light_max , light_mean,avg_mood])
