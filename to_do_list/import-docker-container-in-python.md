# 还能在Python里调用Docker容器？！

## Why would you do this?

Docker containers are awesome for isolating applications from each other, but what if you want them to talk to each other? For instance, if you're developing an app in python that needs to interact with software written in another language. There are a few techniques for achieving low-level interoperability between Python and other popular languages. But if you have a weird case, or some complex legacy software, this becomes difficult or impossible.

## The idea: containers as modules

We created sidomo - Simple Docker Module* so that if you can get your weirdo app to run in any linux environment, then you can instantly call it from Python with zero added effort.

Right now most people use the Docker Daemon API to manage containers carrying their apps. (Kubernetes / Mesos are great examples of this). Sidomo opens up a whole new use case for containers—turning weirdo software into nice, plain vanilla python modules that work seamlessly in python code.

*not an AWS service

## How to use sidomo
Make sure you have docker installed and a docker daemon running. If you're not sure if this is the case, run docker ps and see if you get "CONTAINER ID ..." as output. If you aren't sure how to get docker set up properly, you can check out this link or search here to find your way.

## Setting up Sidomo: a one-liner
You can install sidomo directly from the git repository using pip. Just run the following command in your shell:

pip install -e 'git+https://github.com/deepgram/sidomo.git#egg=sidomo'  

## Example: a simple Hello World

This will start a container from the ubuntu base image, run echo hello from and then echo the other side, and print the lines of output from the process. To prepare for this example, you need to pull the ubuntu image to your machine with one shell command.

### shell

# Get the latest Ubuntu image
docker pull ubuntu  

### Python

from sidomo import Container

with Container('ubuntu') as c:  
    for line in c.run('bash -c "echo hello from; echo the other side;"'):
        print(line)

## Example: wrangling FFMPEG with sidomo

Now let's actually do something useful with sidomo. FFMPEG is a somewhat complex piece of software that manipulates media files efficiently for almost any purpose, but it's not easy to install consistently on different platforms, and there are no up-to-date python bindings for it. With Sidomo, you can pull FFMPEG with docker and easily run it from Python.

shell

docker pull cellofellow/ffmpeg

Python

The example below will grab audio from a URL, transcode it, and print debug messages to prove that it worked. The process's stdout (the raw audio output) is disabled since we only want to see the debug messages.

from sidomo import Container  
url = 'http://www2.warwick.ac.uk/fac/soc/sociology/staff/sfuller/media/audio/9_minutes_on_epistemology.mp3'  
with Container(  
    'cellofellow/ffmpeg',
    stdout=False
) as c:
    for line in c.run(
        'bash -c \"\
            wget -nv -O tmp.unconverted %s;\
            ffmpeg -i tmp.unconverted -f wav -acodec pcm_s16le -ac 1 -ar 16000 tmp.wav;\
            cat tmp.wav\
        \"\
        ' % url
    ):
        print line

If you wanted to actually save the transcoded audio from this process, you would replace the line stdout=False with stderr=False and make sure to write each line of output from the container process (raw audio data) to a file.

## Fun in the future

If you have to write python bindings for some complex software, consider containerizing that software instead. With sidomo, turning a containerized application into a python module is painless and clean.

If you find yourself using subprocess frequently to interact with code for which proper bindings do not exist, then containerizing these processes may make some things simpler.

If you use sidomo in a python app that ends up developing complex dependencies, you may need to wrap the app in its own container and call it from an app with fewer dependencies on the outside. Sidomo supports this as well, since docker supports nested containers. You can make your own software matryoshka doll by using sidomo to import sidomo to import sidomo....

Good luck! Just remember, you can't containerize away complexity indefinitely. Or can you?

原文：[DeepGram](http://blog.deepgram.com/import-a-docker-container-in-python/)