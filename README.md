# object-recognizer


Download and install the cli tool conda.

We use this to install the necessary dependencies. Therefore, in the Command Line:

conda env create --file environment.yml --name=recognizer-env

Then choose the correct python interpreter in your IDE of the newly created environment.


You can install new dependencies by

conda install ...

and export your dependencies into the environment.yml with:

conda env export --no-builds -c conda-forge