#!/bin/bash
root=./swagger_client_L3S
client_name=l3s_recsys_client
json_file=json_file/l3s_recsys_api.json
json_file_dir=$root/$json_file

dir=$root/client

swagger-codegen generate -i $json_file_dir -l python -o $dir -DpackageName=$client_name