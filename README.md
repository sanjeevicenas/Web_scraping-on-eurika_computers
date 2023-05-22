# Web_scraping-on-eurika_computers
This project performs a data acquisition, pre-processing, and data analysis pipeline for a website called eurieka.ie that sells laptops and notebooks. The process involves extracting information about the laptops from the website, cleaning the data, loading it into a MongoDB database, and then performing data analysis on the data.

Firstly, we have imported the necessary libraries such as requests, pandas, and BeautifulSoup to help with web scraping. The requests library is used to send a GET request to the specified URL and receive the response from the server, while BeautifulSoup is used to create a BeautifulSoup object from the HTML content of a web page. The pandas library is used to manipulate and analyze data in a DataFrame.

The code extracts the HTML content from the response and uses BeautifulSoup to find the unordered list element containing the items for sale. If the unordered list element is found, the code proceeds to extract the relevant information from each item in the list. The relevant information for each item includes the item name, the final price (including tax), and the VAT.

The code then stores the extracted information in a list of dictionaries and converts this list of dictionaries into a Pandas DataFrame for processing. The data cleaning is performed in the DataFrame by converting the final price and VAT columns from strings to float and removing leading and trailing whitespace from the item name column.

The code then uses the pymongo library to connect to a MongoDB database and inserts the cleaned data into a MongoDB collection. The code also retrieves the data from the MongoDB collection and displays it in a Pandas DataFrame for performing the data analysis.

Finally, the code performs some data analysis on the cleaned data by creating a scatter plot of final price against VAT, a heatmap of the correlation between final price and VAT, and a histogram of the data.

In summary, the above code performs a pipeline of data acquisition, pre-processing, and data analysis on a website that sells laptops and notebooks. It extracts relevant information from the website, cleans the data, stores it in a MongoDB database, and performs some data analysis on the data.
