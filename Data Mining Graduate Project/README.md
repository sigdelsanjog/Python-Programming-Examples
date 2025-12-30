# Apache Spark Tutorial
## Installation Guidelines
### Prerequisites:
 - Plugin for Scala Programming Support
 - iPython & Jupyter Notebook 
 - Apache Spark Module for Python: pyspark

#### Plugin for Scala Programming Support
Since Apache Spark requires Scala easiest way to get in isntalled on your machine is via Pycharm Installation

- Download Pycharm from the link below:

    https://www.jetbrains.com/pycharm/download/
 - Install Pycharm and get the Scala Plugin support installed

#### iPython Installation
ipython can be installed via pip command <code> pip install ipython</code>

#### Jupyter Notebook Installation
Install notebook via pip: <code> python3 -m pip install jupyter</code>


####  Apache spark Module for Python: pyspark
Install pyspark via pip <code> pip install pyspark</code>

## Run apache spark and Jupyter Notebook

After successful installation of all necessary modules and plugins, load run apache spark server over Jupyter notebook where we will be running our code to run the Apache spark functionalities:

 - In your terminal type <code>pyspark --master local[2]</code>

 This runs jupyter notebook with creation of psaprk server usign two nodes in your localhost server

Next download the following Jupyter Notebook and import(Upload) it on your localhost server:
- Filename: pyspark-traffic-modeling.ipynb

Download following two datasets from the repository and configure the path of these datasets on your Jupyter Notebook:

 - Dodgers.data
 - Dodgers.events

 After configuring the paths you can simply execute the steps available in your Jupiter Notebook one by one to understand how RDDs are manipulated with APache Spark

 Next in order to observe some of the Data wrangling processes and also to observe the MapReduce function downlaod the following Notebook and upload it on your Localhost server.

 - Notebook to Upload: NYPD.ipynb
- Filename: NYPD_Felony.csv

After the download make the changes in file path to laod the dataset as a RDD in your Notebook