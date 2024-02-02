# CI - CD

## step 1

1. generate a key pair using command

```
ssh-keygen -m PEM -t rsa -b 4096
```

2. this will prompt the user to enter the file name of the key pairs, in my case i have given ritwk_key

it will create two files, ritwk_key and ritwk_key.pub

## step 2

1. open the ritwk_key file and copy every single line, it should be like this

```
    ----BEGIN RSA PRIVATE KEY-----
    ..... code ....
    -----END RSA PRIVATE KEY-----
```

2. then go to your github repo's settings -> security -> secret and variables -> actions

3. make three new repository secret (without the double quote)

   a. "SERVER_SSH_KEY" should be the name and the copied secret from the ritwk_key should be the secret

   b. "SERVER_HOST" should be the name and hostname or primary ip of the server where we need to deploy the project should be the secret (in my case i have used the hostname)

   c."SERVER_USER" should be the name and give the username of the server, in my case i have used root.

4. and finally copy the entire content of ritwik_key.pub and go to your server and go to this directory ~/.ssh and edit the authorized_keys file and paste it.

## step 3

go to your github repo and change the conf file and configure your github username and github token

after configuring it should look like this

```
https://_YOUR_GIHUB_USERNAME_:_YOUR_GITHUB_TOKEN_@_REST_OF_THE_GITHUB_URL
```

## step 4

    1. in out project directory where we have out .git, create a new folder named .github and inside .github create a new folder named workflows
    2. and create a new .yml file, in my case i have named my file ci-cd.yml

    3. inside the yml file paste the below code, and make sure the indentation is correct.

    4. you can add or remove the lines from scripts based on the needs.


    ```
        name: CI/CD Workflow
        on:
        push:
            branches: ["development"]
        jobs:
        deploy:
            runs-on: ubuntu-latest
            steps:
            - name: Update Odoo and Restart
                uses: appleboy/ssh-action@v0.1.10
                with:
                host: ${{ secrets.SERVER_HOST }}
                username: ${{ secrets.SERVER_USER }}
                key: ${{ secrets.SERVER_SSH_KEY }}
                port: 22
                script: |
                    cd /odoo/custom/addons/test_odoo
                    git pull origin development
                    sudo service odoo-server restart

    ```

## step 4

as soon as you commit this, in your github repo's actions section you will be able to see the an action running with the same name as the commit.,

if it fails then check there will be an option to re-run all jobs, check the enable debug logging and check the log if everything is correctly done

# Possible Errors

detected dubious ownership in repository .....

it is because while setting up odoo, we have made a different user, and that user have the permission to access the repository. to change this go to your root user, and try to access the directory.

if you see the the same error here
(detected dubious ownership in repository .....)
then it will give you a command for solving the issue or else you can use the below code

```
git config --global --add safe.directory /path/to/your/repo
```
