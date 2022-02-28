# Surfs_up
## Overview of Project
>This project is based on a given Sqlite format data, to analyze the temperature data for determine the weather situations on June and December. Main purpose is using the filters and description functions to find an intended results.
### Methods
> Jupyter notebook and Sqlalchemy were used for the purposes of the project. This allows us to work easily without using a server for databases and gave us a quick results. Also help us to get acquinted of the both platforms. First step of the project is create an engine an session as a preperation of connecting a databse. Then filters were applied and instead of getting a whole database, expected parts exported and turning into a dataframes to work and analyze easily. Last step is using the describe function to see the average, mean, min and max values of specific months. 
## Results
> Weather conditions are most likely similar to each other throught the year, since we've check both June and December. Even though some days could be slightly colder than expected, we can say whole year approximately fits for intended business purposes. In December we could see the high temperatures almost as high as summer.
## Summary
> In conclusion, we've worked on jupyter notebook with Sqlalchemy to use the databases without connecting and opening a server. It gives users to mobility and ease of access. Quick analysis and determinations can be done easily. After the analysis conclusion can be summarized as the weather of Oahu is good for business for an entire year. This conclusion determined based on checking the June and December summary statistics between the year 2010 and 2017( by the given dataset). Following pictures are the results of analysis. 
> ![Analysis](/surfs_up/June.png)                      ![Analysis2](/surfs_up/Decemeber.png)
