#!/bin/bash

check_validator () {
  did_pass=$1
  validator_name=$2
  if [ $did_pass -eq 0 ]
  then
    echo "${validator_name} passed successfully"
  else
    echo "${validator_name} did not pass"
    exit 1
  fi
}

variable=$1
pycodestyle --exclude='./venv*'
check_validator $? "Pycodestyle"
pydocstyle
check_validator $? "Pydocstyle"

echo "Validation Passed!"