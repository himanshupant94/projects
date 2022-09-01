# Create a lambda layer in zip package from dockerfile

- Take Amazon linux image from dockerhub and enable amazon lib and install python,zip modules
- Install python modules using pip3.8/pip/pip3 (depend on your requirement)
- Create zip file and extract zip file from image using below commands
- Build Docker Image: `docker build- --progress=plain -t IMAGE_NAME(test) -f dockerfile .`

- Run `docker create -ti --name dummy IMAGE_NAME bash`

  **Example:** `docker create -ti --name dummy test bash`

- Run `docker cp dummy:/out/build/oracle/ .`

- Run `docker rm -f dummy`
