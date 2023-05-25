#!/bin/bash
args_array=("$@")
for i in "${args_array[@]}"
do
  :
  echo "### Got variable $i ###"
done

if [ -z "$script_name" ]; then
    echo "script_name is NOT configured, Script will exit !"
    exit 
else
    echo "script_name passed is: '$script_name'"
    case ${script_name} in
    'app.py')
        python app.py "$@"
        echo "### Got ip ###"
    ;;
  esac 
 fi