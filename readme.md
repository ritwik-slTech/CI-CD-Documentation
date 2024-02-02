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

`----BEGIN RSA PRIVATE KEY-----`
`..... code ....`
`-----END RSA PRIVATE KEY-----`

2. then go to your github repo's settings -> security -> secret and variables -> actions

3. make three new repository secret (without the double quote)

   a. "SERVER_SSH_KEY" should be the name and the copied secret from the ritwk_key should be the secret

   b. "SERVER_HOST" should be the name and hostname or primary ip of the server where we need to deploy the project should be the secret (in my case i have used the hostname)

   c."SERVER_USER" should be the name and give the username of the server, in my case i have used root.
