#!/bin/bash


source ./setup_can.sh


Usage() {
cat << EOF
$0 route data_dir
	route : 1fc693fc142f4646_2021-01-22--13-22-45
	op_data_dir: ~/work/op_data/all/
example:
$0 1fc693fc142f4646_2021-01-22--13-22-45 ~/work/op_data/all/
EOF
}


if [ $# -ne 2 ]
then
  Usage
  exit 
fi

#export PYTHONPATH=~/openpilot-master-tools
export PYTHONPATH=~/openpilot
$PYTHONPATH/tools/replay/unlogger.py $1 $2
