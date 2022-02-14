# checkpoint-find-disabled-rules
Python script to find disabled rules in the "Network" layer of a Check Point rulebase. 


This script connects to the Check Point management API in a secure way. Root certificate of the Management server should be named as "rootca.cer" and located in the same directory with the script. If you want to skip SSL verification you can set verify parameter as False without using quotes.

There is a default limit to return 500 results per request. This script works for the first 500 results. Improvement is required to check more rules.
