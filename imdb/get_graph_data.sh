#!/bin/bash

while read p; do
	IFS=',' read -r -a arrP <<< "$p"
	echo ${arrP[2]};
	wget --load-cookies='cookies.txt' --page-requisites "${arrP[2]}";
done <stars_out2.txt

