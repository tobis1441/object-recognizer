# object-recognizer

## Setup workspace

Download and install python 3.10.14. This download should include pythons package manager "pip". Verify this by typing in the command line:

`pip --version`

We use pip to install the necessary dependencies. 
First we setup a virtual environment, where the dependencies will be saved to. This is to not clash with any global dependencies AND make the environment repoducable.
The necessary dependencies and version are listed in the requirements.txt file.
### Create the virtual environment
`python -m venv object-recognizer-env`

### Activate the virtual environment
On Windows then activate the environment with:
`object-recognizer-env\Scripts\activate`

On Linux/macOs:
`source object-recognizer-env/bin/activate`

### Install the dependencies
Then, in the Command Line type:
`pip install -r requirements.txt`

Then choose the correct python interpreter in your IDE of the newly created environment.

Now download the model from:

https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/

rename it to model_retinanet.pth and put it at root level of project.

You now should be able to run main.py and get printed out the result from object recognition in the given image.

## Further workflow
You can install new dependencies in a terminal with the activated virtual environment by

`pip install NAME_OF_LIBRARY`

and export your current env:

`pip freeze > requirements.txt`.



# Run as container

Build the image by:

`docker build -t object-recognizer .`

Then run the service via:

`docker run -p 8000:8000 -d object-recognizer`