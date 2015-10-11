#!/usr/bin/env bash

function run() {
  cmd_output=$($1)
  return_value=$?
  if [ $return_value != 0 ]; then
    echo "Command '$1' failed"
    exit -1
  else
    echo "output: $cmd_output"
    echo "Command succeeded."
  fi
  return $return_value
}

cd /home/ubuntu/python-crossbarhttp/

sleep 5

run "coverage run --source=crossbarhttp crossbarhttp_tests.py"
cp .coverage /data/.coverage

sleep 1
