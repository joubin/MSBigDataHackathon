#MSBigDataHackathon
---

### -- Hakathon Goals --

Take a huge data set from Seattle Gov and use HDInsight  '_Hadoop_' to query the data and then either model it or use it for predictive analytics and/or machine learning. 

###### Requirements
* __DO NOT__ apply Azure passes for current subscriptions '_will invalidate the pass_'
* We __MUST USE__ the tools demoed, __HDInsight__ to consume the data and __PowerBI__ to visualize


### -- Project Notes --

##### The Hackathon Project Team 

| First Name   | Last Name     | Email                     |
| ------------ | ------------- | ------------------------- |
| Joubin       | Jabbari       | <joubin.j@gmail.com>      |
| Steven       | Brower        | <sbrower@vt.edu>          |
| Dustin       | Arendt        | <Dustin.Arendt@gmail.com> |
| Chris        | Carpenter     | <Chris@bienabee.com>      |
| Louis        | Tadman        | <Louis@bienabee.com>      |


###### Data Sources from [Seattle Gov](https://data.seattle.gov/)
* [Land Use Permits](https://data.seattle.gov/Permitting/Land-Use-Permits/uyyd-8gak)
* [Building Permits](https://data.seattle.gov/Permitting/Building-Permits-Current/mags-97de)
* [Seattle Police Department 911 Incident Response](https://data.seattle.gov/Public-Safety/Seattle-Police-Department-911-Incident-Response/3k2p-39jp)
* [Public Outreach and Engagement Events](https://data.seattle.gov/Community/Public-Outreach-and-Engagement-Events/8pec-7ugc)
* [My Neighboprhood Map '_Community Amenities_'](https://data.seattle.gov/Community/My-Neighborhood-Map/82su-5fxf)



### -- General Presentation Notes --

These are general notes and ideas from interesting topics and discussions with other hackathon members


### -- Hadoop --

#### System used as a way to process massive data sets

* Link to [Hadoop](https://hadoop.apache.org/) and to [HDInsight](http://azure.microsoft.com/en-us/services/hdinsight/)
* HDInsight is Hadoop as a service on the Azure platform
* HDInsight on Azure has blob storage for saving and preserving data once your Azure platform is spun down
* Every HDInsight cluster must have a head node and data nodes

### -- Machine Learning --

#### Computer systems that improve with experince based off of historical data

* Azure has a [Machine Learning](http://azure.microsoft.com/en-us/services/machine-learning/) platform
* Example of machine learnign is mail sorting alrogythms that learns multiple different handwriting styles and is able to understand and process addresses
* Kinect has machine Learning, a lot of current MSFT software has machine learning
* [R](http://www.r-project.org/) & [Python](https://www.python.org/) are good languages to use for machine kearnng programming
* To process data with Azure machine learning the data must be in Azure '_HDInsight_' for example
* Uses RESTful API and deals with JSON data

###  -- Power BI --

#### Power BI is a business inteligence visualization tool 

* PowerBI can be used for free and accessed at [PowerBI](http://http://powerbi.microsoft.com/)
* PowerBI has excellent integration with iPhones by using the Microsoft PowerBI application
* You can use the [PowerBI Designer](https://powerbi.microsoft.com/designer) as a canvas to create your report visualizations

![Initial structure of our program](http://i.imgur.com/O5P4hsm.jpg)
