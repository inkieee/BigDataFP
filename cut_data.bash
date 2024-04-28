#!/bin/env bash

input_file='aqi_daily_1980_to_2021.csv'
output_file='aqi_daily_2016_to_2021.csv'

#data range 1980-01-01 is second column of data (hence $2 of awk)

awk -F ',' ' ($2 >= "1980-01-01" && $2 = "2016-12-31") {next} {print} ' $input_file  > $output_file
