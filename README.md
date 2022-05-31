
# parse-bsvdm


You can use this script to parse the AIS base station files and make them look like they came from a boat.

All this needs to do is take the original line, strip off the time stamp, change the sentence prefix and then calculate the new checksum.

This script will take a specified log file that contains valid BSVDM and BSVDO entries and writes a new file with the AIVDM and AIVDO equivalents.

My current source file is from the public feed from the Norwegian Coastal Administration.

I simply use putty to generate log files by pointing to the data source and collecting data.

My needs are limited. I just need to collect data to a log for short periods and then process it.

More information can be found here: 

https://kystverket.no/en/navigation-and-monitoring/ais/access-to-ais-data/