# Docker lecture

**part 1 theory - what is docker**

<a href="https://youtu.be/TNX1LuV2Ljs" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/docker_intro_theory.png?raw=true" alt="docker theory" width="600">
</a>


**part 2 coding**


<a href="https://youtu.be/lAckpoLox5g" target="_blank">
<img src="https://github.com/kokchun/assets/blob/main/data_platform/dockerfile_code.png?raw=true" alt="docker image coding" width="600">
</a>


In this lecture you'll learn the basics of Docker and containerize a Python application. We will work extensively with command line tools (CLI) so make sure to learn the commands.

Follow instructions in resources lecture 04 to install docker on your machine.

---

## Creating a Python docker container

 We need some instructions so that we can **build** an **image** of how the container should look like. From this image we can then **spin** up as many containers as we want from this image, and they will have the same configurations. We'll write the specifications in a Dockerfile.

```bash
touch Dockerfile
```

Now lets use Python 3.11 as a base image, and create a file called main.py with a short print statement inside.

```Dockerfile
# gets python3.11 image from Dockerhub with their configurations, so we don't have to manually install Python3.11 as we do in our own machine
FROM python:3.11

# specifies where the entry point is for our docker container to start in 
WORKDIR /app

# adds everything in this folder into the app directory of the container
COPY . .

RUN pip install -r requirements.txt

# run these commands when the docker container is run
CMD ["python", "app.py"]
```

Now we should have an actual python file, so copy the code from app.py in this folder. Then we should also have a requirements so that the container can install pandas, so create requirements.txt and add pandas to it.


Building time

```bash
# builds the image with repository name first-python-app and tag latest
# can choose to tag it something else using : e.g. first-python-app:v1
docker build -t first-python-app .

# check the image
docker image ls

# if you have many images use to search for it
docker image ls | grep python
```

Woah that was fast and efficient, time to spin up our container, an analogy to OOP is that image is a class and container is an instance of that class. Spin spin spin ...

```bash
# spins up a container by name first-app using first-python-app as image
docker run --name first-app first-python-app
```

Isn't that supercool, we see our Python program is running with the supercool printing message.

```bash
# probably we don't see any containers, as ours have closed
docker container ls

# now this lists all containers, including closed ones
# also pipe with grep if you have many containers and need to find a particular one
docker container ls -a
```

Cool, that we ran the container, but let's dive deeper to find out what the container is and what it contains (höhö)

```bash
# -it flag for interactive mode, /bin/bash opens up a bash shell inside the container
docker run -it first-python-app /bin/bash
```

Imagine you have come into a new world that was isolated from your current world, but you could before just see the surface. Now you have found the key to unlock its secrets, so dig in and explore

```bash
whoami # root
date
echo "My OS is: $OSTYPE"
pwd # /
ls -al
which python
ls | grep main # seems like our script got copied to the root
cat main.py
python main.py
mkdir cool_src_code
mv main.py cool_src_code
```

So we can run a python shell inside the container

```py
import sys
sys.version 

from datetime import datetime
datetime.now() # another time zone

quit() # or ctrl+D to get out
```

Now we shut down our container by ctrl+D, we can check that our container is closed

```bash
docker container ls -a

# note that this spins up a new container from the same image
docker run -it --name first-python-app first-app /bin/bash

# we see that the changes we made is not here as this is a new fresh container
ls
```

Okay jump out with ctrl+D and inspect our containers created

```bash
# ah there are two containers
docker container ls -a 
```


---

## Clean up containers and images

Lets reset and remove all containers and images that are not running

```bash
docker container prune && docker image prune
docker image ls
docker container ls -a
```

Wupp wupp we have dockerized our first app, the app doesn't do much than printing out a dataframe and a version but still cool
