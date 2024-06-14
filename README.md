# object-recognizer


Download and install the cli tool conda.

We use this to install the necessary dependencies. Therefore, in the Command Line:

conda env create --file environment.yml --name=recognizer-env

Then choose the correct python interpreter in your IDE of the newly created environment.


You can install new dependencies by

conda install ...

and export your dependencies into the environment.yml with:

conda env export --no-builds -c conda-forge




Now download the model from:

https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth/

rename it to model_retinanet.pth and put it at root level of project.

You now should be able to run main.py and get printed out the result from object recognition in the given image.