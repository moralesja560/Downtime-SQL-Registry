# Downtime-SQL-Registry
App to upload downtime records to a SQL database.

We currently use an Excel file to track every machine downtime during the shift. Machine breaks down, we fix it, and a Maintenance Order is filled by the affected station. This Maintenance Order (MO) contains various fields such as:

* Machine Name
* Date
* Failure time
* Repair time
* Line
* Operator and Maintenance Tech signatures
* Failure Description
* Repair Description.

When the MO is uploaded to the Excel database, we break down the failure to component level and we add a probable root cause. We do this to fit the data into already-defined categories. This helps with posterior data analysis and postprocessing.

Now it's time to migrate that database to a SQL table where we can protect the data. This repository contains the software the end user will upload the data through. 

The end user will keep the familiarity, because the software will look like the old Excel VBA Userform that i designed. The only extra stuff is an indicator for the end user to see if the SQL server is online and some other SQL parameters that will be prefilled. The user will only need to test the connection and start filling the form.
