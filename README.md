![Python](https://img.shields.io/badge/python-3.12.3-blue.svg) 

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
    3. JDK 17 installed (8, 11 or 17 are compatible with spark 3.4.0)
       1. You will need to add this to you're `.zshrc`: `export JAVA_HOME=\$(/usr/libexec/java_home)`
3. Clone this repository 
4. You can run the tests locally yourself by doing the following (it is recommended that you manage your python environments with something like [asdf](https://asdf-vm.com/) and use python==3.12.3 as your local runtime):
    
    ```sh
    python -m venv venv  # this sets up a local virtual env using the current python runtime
    source ./venv//bin/activate  # activates the virtual env
    pip install -e ."[dev]"  # installs this packages in local env with dependencies
    pytest . -r f -s   # -r f shows extra info for failures, -s disables capturing
    ```
   1. If everything installed without issue then test that pyspark works, open a fresh terminal and type `pyspark` and hit enter. This is dependent upon setting JAVA_HOME in the earlier step. `exit()` out of this if it worked.
   2. You need to follow the steps in the [Getting Started](https://hadoop.apache.org/docs/current/hadoop-aws/tools/hadoop-aws/index.html#Getting_Started) section for connecting to S3, see also StackOverflow posts [like this one](https://stackoverflow.com/questions/44411493/java-lang-noclassdeffounderror-org-apache-hadoop-fs-storagestatistics/44500698#44500698) for clarifications. The important thing is that you install these 2 JARs in the pyspark classpath and that their versions match each other:
      1. **hadoop-aws** JAR must match the version of hadoop required by this version of spark. Spark 3.4.0 requires hadoop 3.3.4.
      2. the **AWS SDK For Java Bundle** JAR - this one you need to find the version that hadoop-aws was created with by looking at its [dependencies](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/3.3.4). For hadoop-aws 3.3.4 this is 1.12.262.
   3. The installed by navigating to something like the following:
   ```shell
   cd venv/lib/python3.12/site-packages/pyspark/jars/
   curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
   curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
   ```

5. From within this repository run the following:
  
    ```sh
    terraform init
    terraform workspace new dev  # this should switch you to the dev workspace
    terraform plan -var-file="dev.tfvars" -out=dev-plan.out
    terraform apply -var-file="dev.tfvars" dev-plan.out
    ```
   
    For deploying to prd

    ```sh
    terraform workspace new prd  # or terraform workspace select prd if already created
    terraform plan -var-file="prd.tfvars" -out=prd-plan.out
    terraform apply -var-file="prd.tfvars" prd-plan.out
    ```
   
   On subsequent updates you don't need to `init` or make a new workspace again.