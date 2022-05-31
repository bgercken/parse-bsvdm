
# parse-bsvdm


You can use this script to parse the AIS base station files and make them look like they came from a boat.

This script will take a specified log file that contains valid BSVDM and BSVDO entries and writes a new file with the AIVDM and AIVDO equivalents.

All we do is take the original line, strip off the time stamp, change the sentence prefix, calculate the new checksum and reassemble the sentence.

Currently the AIS source data that I am using is from the public feed provided by the Norwegian Coastal Administration.

To collect data I simply use putty to generate log files by pointing to the data source.

My data collection needs are limited. I just need to collect data to a log for short periods and then process the data using a separate program.

More information about the NCA data feed can be found here: 

https://kystverket.no/en/navigation-and-monitoring/ais/access-to-ais-data/
