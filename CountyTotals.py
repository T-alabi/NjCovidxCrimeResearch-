import numpy as np 
# needed imports 
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import mysql.connector

#connection to persona DB
mydb=mysql.connector.connect( host="Your host",
                             user = "Your User",
                             password= "Your Padd",
                             database= "Your DB")

#labeleing the histogram bars 
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha='center')

#declaring the curser for the SQL statement 
mycursor=mydb.cursor()
mycursor.execute("select County, caseNum, deathNum from 2023S_oalabi.CountyTotals order by County;")
result = mycursor.fetchall

#variables in the SQL statement 
county = []
caseNum = []
deathNum=[]
colors=['blue', 'green', 'black', 'limegreen', 'black', 'grey', 'black', 'red', 'coral', 'sienna', 'orange', 'gold', 'lightgreen', 'cyan', 'dodgerblue', 'steelblue', 'darkblue', 'indigo', 'palevioletred', 'purple', 'orchid', 'black']

#add sql results to the vars
for i in mycursor:
    county.append(i[0])
    caseNum.append(i[1])
    deathNum.append(i[2])

#graph titles and labels 
plt.xlabel("Days in 2020")
plt.ylabel("Case numbers")
plt.title("Case numbers in NJ counties over the year 2020 ")
#this removes the x axis words from the SQL statement so theyre just in the ledgend 
plt.xticks([])

#setting the colors for the bar chart ledgend 
plt.bar(county, caseNum, color=colors)
legend_elements = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
plt.legend(legend_elements, county, bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)

#adds the number labels to the bar
addlabels(county, caseNum)

#show the graphic bar chart
plt.show()






