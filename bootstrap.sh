#!/bin/bash
curl -L https://www.opscode.com/chef/install.sh | sudo bash
chef-apply -e "package 'docker.io'; execute 'docker.io run --name test_container -d -p 80:80 -p 3306:3306 kobrinartem/lamp:wordpress'"
