import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
import matplotlib.pyplot as plt




Opinion = int(input("On a scale of 1-10 how good are period tracking apps in your opinion: "))
Time = int(input("How often do you use period tracking apps on a scale of 1-12: "))
Wellbeing = int(input("On a scale to 1-10 how do period tracking apps improve your wellbeing: "))
avg_mood = round(mean([Opinion,Time,Wellbeing]),2)

print("My expierience with peroid tracking apps is  ", " ", avg_mood)

file_path = 'Robyn-MicrobitData.csv'

with open(file_path, 'r', newline='') as csvfile:
 
    csv_reader = csv.reader(csvfile)
    
    
    for row in csv_reader:
        
        print(row)  

df = pd.read_csv('Robyn-MicrobitData.csv')
Good_min = df['Good'].min()
Good_max = df['Bad'].max()
Good_mean = df['Needswork'].mean()
print ("Min = ",Good_min,"Max = ", Good_max, "Mean = ",Good_mean,"Average Mood= ", avg_mood)

df = pd.read_csv('Robyn-MicrobitData.csv')

sizes = [1,2,3]
labels = 'Good', 'Bad', 'Needs Work'  
colors = ['blue', 'purple', 'lightskyblue']
explode = (0.1, 0.0, 0.0)  
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title("Piechart")

plt.show()



#f = open("BR1-3_results.csv", "a", newline='')





 


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
