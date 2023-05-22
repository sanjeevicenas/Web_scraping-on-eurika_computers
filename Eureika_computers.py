import requests  
import pandas as pd
from bs4 import BeautifulSoup
url='https://www.eurieka.ie/computers/laptops-notebooks.html?gclid=Cj0KCQjwi46iBhDyARIsAE3nVraV5SidiGk-pWoJmiUu6DTLjbHW9OaZGmgApzE27FSRBQvRsIVPypQaAtnFEALw_wcB'
resp=requests.get(url) #Sends a GET request to the specified url using the requests library in Python.The response from the server is then stored in the resp variable
resp
resp.content   # content of the response received from the server
soup=BeautifulSoup(resp.content) #creates a BeautifulSoup object from the HTML content of a web page that was obtained from a HTTP response using the requests library.
soup
ul = soup.find('ol', {'class': 'products list items product-items'})
items = ul.find_all('li', {'class': 'item product product-item'})
ul = soup.find('ol', {'class': 'products list items product-items'}) 

if ul is not None:
    items = ul.find_all('li', {'class': 'item product product-item'})
    leng=len(items)
    print(leng)
else:
    print('Could not find the unordered list element')

if items:
    first_item = items[0]
  
else:
    print('No items found')

info=[]
for item in items:
  record={}
  record['Item name']=(item.find('strong',{'class':"product name product-item-name"}).text)
  record['Final Price']=str(item.find('span',{'class':"price-wrapper price-including-tax"}).text.replace('€',''))
  record['Including VAT']=(item.find('span',{'class':"price-wrapper price-excluding-tax"}).text.replace('\n','').replace('€',''))

  info.append(record)
  
eurieka=pd.json_normalize(info)   #convert this list of dictionaries into a Pandas DataFrame
eurieka['Final Price'] =  eurieka['Final Price'].astype(float) # Pandas library to convert a column of a Pandas DataFrame from one String to float.
eurieka['Including VAT'] = eurieka['Including VAT'].astype(float)

eurieka

eurieka['Item name'] = eurieka['Item name'].str.strip() #remove leading and trailing whitespace from a column of a Pandas DataFrame

eurieka

! python -m pip install pymongo==3.7.2
! pip3 install pymongo[srv]
import pymongo
from pymongo import MongoClient

import pymongo
client = pymongo.MongoClient("mongodb+srv://1234:1234@cluster0.wx1wkmc.mongodb.net/?retryWrites=true&w=majority")
db = client["mydata"]
collection=db['listings']

db

data = eurieka.to_dict(orient='records') #Converts the eurieka DataFrame to a list of dictionaries using the to_dict() method with the orient parameter set to 'records'
for document in data:
    collection.insert_one(document)

data = eurieka.to_dict(orient='records')
for document in data:
  document_dict = dict(document)
  collection.insert_one(document_dict)
  
rdf1 = collection.find({},{"_id":0,"Item name":1, "Final Price":1,"Including VAT":1})
df1 = pd.DataFrame(list(rdf1))
display(df1)

eurieka.info()

eurieka.describe()

#Scatter plot of Final Price vs Including VAT in laptops

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4,3))
ax.scatter(x=eurieka['Final Price'], y= eurieka['Including VAT'],  marker='+')
plt.xlabel("Price") # x-axis label
plt.ylabel("Vat") # y-axis label
plt.title("Scatter plot of Final Price vs Including VAT in laptops") # Title of the chart 
plt.show()

# Heatmap showing correlation between variables in the eurieka dataset.

import seaborn as sns
fig, ax = plt.subplots(figsize=(4,3))                       # Adjusting the figure size
sns.heatmap(eurieka.corr(), ax=ax, annot=True, fmt=".2f")

# Calculation of Total Price based on Final Price and VAT in a DataFrame

df = pd.DataFrame({
    
    'Final Price': [300, 222, 22],
    'Including VAT': [10.99, 5.99, 2.49]
})

# calculate total price column
df['Total Price'] = df['Final Price'] * df['Including VAT']

# display the updated DataFrame
print(df)

# Histogram of eurieka data distribution.

eurieka.hist(figsize=(5,4))