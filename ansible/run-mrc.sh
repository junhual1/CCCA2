#!/bin/bash

# . ./openrc.sh; ansible-playbook -i hosts -vv mrc.yaml --ask-become-pass | tee output.txt
. ./openrc.sh; ansible-playbook -i hosts -vv mrc.yaml | tee output.txt