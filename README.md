
# parse-bsvdm


This script can be used to parse AIS base station sentences (!BS) and make them look like they came from a boat (!AI).

The script will take a specified log file that contains valid BSVDM and BSVDO entries and writes a new file with the AIVDM and AIVDO equivalents. All we do is take the original line, strip off the time stamp, change the sentence prefix, calculate the new checksum and reassemble the sentence.

Currently the AIS source data that I am using is from the public feed provided by the Norwegian Coastal Administration. To collect data I simply point putty to the IP and port described in the NCA documentation below and collect snapshots of data for post processing with this script. The script generates a file with the reformatted lines named after the original with a ".out" suffix appended. For example: nca-putty2022-05-31-172657.log -> nca-putty2022-05-31-172657.log.out

More information about the NCA data feed can be found here: 

https://kystverket.no/en/navigation-and-monitoring/ais/access-to-ais-data/

Notes:

1. If anyone has a pointer to describe the prefix to the base station records could you end it my way? bgercken@gmail.com

Looking to decode the first two fields in a record like:

```
\s:2573310,c:1654088303*0B\!BSVDM,1,1,,A,B3m8E=000h72d?`stqjcCwd5kP06,0*22
```

Thanks.
