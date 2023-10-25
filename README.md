# SYMRISE TEST

This a test realised for Symrise : 

"Data Sources: Immobilienscout24 (offers for flats in Germany) and Bright Sky (Weather data for Germany)

Focus on these cities: Berlin, Cologne and Munich

Output: Visualization of the relative share of flats that have air conditioning.

- Task 1:

Use python to implement a simple analytics pipeline to bring the data together and visualize it with a python library of your choice to show the differences/similarities between cities w.r.t. how popular air conditioning is.

- Task 2:

Add an analysis that shows the impact of the hot season in summer of the likelihood of a flat having air conditioning. Please use the ImmobilienScout24 API to collect data about recent flat offerings. Save the data in a suitable database and create a pyspark based analytics pipeline that connects the ImmobilienScout24 data with the Data of the BrightSky API from the Deutsche Wetterdienst (German weather info service). Try to visualize figures that indicate if hot regions are more likely to have flats with air conditioning.

Expectations: Use gitlab or github for versioning of your project. Focus on the code and architecture, figures should make sense and look decent but a few of them is enough. Think about what can be improved, reason your design decisions, libraries chosen and discuss potential future enhancements."

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following librairies.

```bash
pip install -r requirementx.txt
```
To use pyspark
- install java 8
- set JAVA_HOME and Path variable
- download Apache Spark : ideally the 3.5.0 - Hadoop 3 release
- set SPARK_HOME, HADOOP_HOME, Path environment variables
- set SPARK_LOCAL_HOSTNAME = localhost as environment variable

To use MongoDB Atlas
- create an MongDB account
- create a new cluster
- configure mongodb user
- get credentials to write/read the cluster from MongoDB ATLAS

## Usage

### task 1
```python
testsyrime-git> python -m testsymrise
```
When the first graph appears click close

Then the seccond graph will appear


### task 2
- Open the commande prompt as administrator

- Navigate to the folder where the script is test_spark.py is located 
```python 
spark-submit test_spark.py
```
- Wait at the end, the graph will be displayed in your web browser

## Contributing



## License
