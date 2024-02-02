# CI - CD

## step 1

generate a key pair using command

```
ssh-keygen -m PEM -t rsa -b 4096
```

this will prompt the user to enter the file name of the key pairs, in my case i have given ritwk_key

it will create two files, ritwk_key and ritwk_key.pub

open the ritwk_key file and copy every single line, it should be like this

`----BEGIN RSA PRIVATE KEY-----`
`..... code ....`
`-----END RSA PRIVATE KEY-----`
