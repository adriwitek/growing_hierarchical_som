# SOM Analytic Tool

Graphic Interactive Tool for Data Analysis and Visualization with Self Organized Maps.


## Introduction
 Self Organized Maps Algortihms are Unsupervised Artificial Neural Networks able to map  high-dimensional relationships in data into a low-dimensional, discretized space.
 Inspired in neurobiology , they change their internal structure in response to stimulus. Similar paterns are located in the same regions of space(just like human brain, different functions are located on different regions of the cortex).


## About the Tool
This is a graphic interactive tool for data analysis and visualization with self organized maps algorithms based on Dash.
  3 Algorithms are avaible at this tool:

  * Classic SOM (Self Organized Map):  Also known as Kohonen Maps.
  * GSOM(Growing Self-Organizing Map): A som that grows depending on data input.
  * GHSOM(Growing Hierarchical Self-Organizing Map): A hierarchical tree structure made with GSOMs that can grow  both vertical and horizontal depending on input data dristribution, showing the data relationships.

![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/cargar.gif "App Home Screen")



## Requeriments
Versions are important, since different packege versions in some libraries cause some problems!

| Software  | Version |
|:--------------------------------------------------------------:|:-------:|
| [Python](https://www.python.org/downloads/)                    | 3.8.3  | 
| [Dash](https://dash.plotly.com/installation)                   | 1.19.0 | 
| [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)  | 0.11.3 | 
| [Python Dateutil](https://pypi.org/project/python-dateutil/)                      |  2.8.1| 
| [Cycler](https://pypi.org/project/Cycler/)                      | 0.10.0 | 
| [Kiwisolver](https://pypi.org/project/kiwisolver/)                      |1.0.1  | 
| [Pandas](https://pypi.org/project/pandas/)                      | 1.2.4 | 
| [Networkx](https://networkx.org/)                      | 2.5| 
| [Scikit-learn](https://scikit-learn.org/stable/install.html)                      | 0.24.1 | 
| [matplotlib](https://matplotlib.org/)                          | 3.4.1   |
| [NumPy](http://www.numpy.org/)                                 | 1.20.2  | 
| [ProgressBar 2](https://pypi.org/project/progressbar2/)        | 3.37.1  | 
                 
## Installation
I recommend creating first an enviroment like conda to avoid package version problems:
```python
 conda create --name som_app_env
 conda activate som_app_env
 ```
And then install the dependencies:
```python
 pip install -r requirements.txt 
 ```
 
## Run
Open a python terminal on app's directory an then run:
```python
 python tool.py 
 ```
Then just go to http://localhost:8050/ on your Web Browser(You can click on direction on terminal showing after runnig previous command )
Remember to have activated your enviroment before runnign




## Some Functionalities Included...
#### Save/Load Trained Models
Trained models will be under **'/Trained_Models'** path. It's necessary to locate there trained models so they can be loaded by the app
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/load.gif "App Load Screenshot")


#### Anomaly Detector
Potencial anomalous detected data on SOM's models can be saved as a .csv to be examined later or under other tools. 
This .csv files will be located on **'/Anomalies_Detected'** path , where it can be moved, since app wont use them directly.

![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/anomalies.gif "App Anomaly Detector Screenshot")






## Some App Screenshots...


#### Error Progress
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/training%20animation.gif "App Screenshot")

#### SOM Multi-Train
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/som_multi_train.png "App Screenshot")

#### Component Plans Minimum Hit Filter 
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/slider.gif "App Screenshot")

#### Auto Hyperparameters Tuning
Searching optimus Hyperparameters:
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/rand_search.gif "App Screenshot")

Search Result:
![alt text](https://github.com/adriwitek/som_analytic_tool/blob/master/Screenshots/rand_search_result.png "App Screenshot")



