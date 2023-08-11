#!/bin/bash
# this script applies necessary changes to files and directories, builds the images, and pushes to aws
# ./buildAndPushDockerImage.sh -a [account_number]

while getopts a: flag
do
    case "${flag}" in
        a) account_number=${OPTARG};;  # 123456789
    esac
done
: ${account_number:?Missing -a}   # checks if these have been set https://unix.stackexchange.com/questions/621004/bash-getopts-mandatory-arguments
echo "account_number: $account_number";

cd ..

# make the predict script executable
chmod +x model/PredictETL.py
# make it so we can write the latest model from S3 to the pickledModels directory
chmod -R +w pickledModels/

# build the base image
echo "Building predict-etl-base image"
docker build -t predict-etl-base:latest -f ./model/Dockerfile .

# build the predict-etl-execute image
echo "Building predict-etl-execute image"
docker build -t predict-etl-execute:latest -f ./model/Dockerfile.execute .

# Push to ECR
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin ${account_number}.dkr.ecr.us-east-2.amazonaws.com
docker tag predict-etl:latest ${account_number}.dkr.ecr.us-east-2.amazonaws.com/predict-etl:latest
docker push ${account_number}.dkr.ecr.us-east-2.amazonaws.com/predict-etl:latest
