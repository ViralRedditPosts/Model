# Viral Reddit Posts Model

The purpose of this repo is to:

1. Conduct Data Science experiments to build a model that predicts viral Reddit posts.
2. Build a reusable ETL pipeline for for both data science development and model deployment.
3. House docker files needed for building an image of the model.
4. Deploy infrastructure and model on AWS ECS.

# How to use

1. First ensure the DynamoDB tables are set up via [DynamoDB-Setup](https://github.com/ViralRedditPosts/DynamoDB-Setup).
2. Installs - see the [prerequisites section on this page](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build#prerequisites) for additional information, the steps are essentially:
    1. Install Terraform CLI
    2. Install AWS CLI and run `aws configure` and enter in your aws credentials.
3. Clone this repository 
4. From within this repository run the following:
  
    ```sh
    terraform init
    terraform apply
    ```
    If you don't want to apply the changes to your aws account you can instead run `terraform plan`.