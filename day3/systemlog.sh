#!/bin/bash

info_count=0
warn_count=0
error_count=0

# Function to analyze log line
analyze_log() {

line=$1

if echo "$line" | grep -q "INFO"
then
((info_count++))

elif echo "$line" | grep -q "WARNING"
then
((warn_count++))

elif echo "$line" | grep -q "ERROR"
then
((error_count++))
fi

}

# Function to determine system status
check_status() {

if [ $error_count -gt 10 ]
then
status="Critical"

elif [ $error_count -gt 0 ]
then
status="Warning"

else
status="Healthy"
fi

}

# Read input file
echo "Enter log file name:"
read logfile

if [ ! -f "$logfile" ]
then
echo "File does not exist"
exit
fi

# Loop through file
while read line
do
analyze_log "$line"
done < "$logfile"

# Determine status
check_status

# Generate report
{
echo "System Log Analysis Report"
echo "--------------------------"
echo "INFO Count: $info_count"
echo "WARNING Count: $warn_count"
echo "ERROR Count: $error_count"
echo ""
echo "System Status: $status"
} > report.txt

echo "Report generated: report.txt"
