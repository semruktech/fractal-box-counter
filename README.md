# Fractal Box Counter
This repository contains a Python script for performing single click fractal box counting on medical images. It can be used for image analysis and fractal dimension calculation in dental research.

### Getting Started
These instructions will help you set up the project on your local machine.

### Prerequisites
Download this repo as a zip file and extract all files to your desired location.

To run the project, the following software needs to be installed on your machine:
- Python>=3.11
- Required Python packages:
  - opencv-python
  - scikit-image
  - numpy

If you already have these software and packages on your machine, proceed to the usage step, otherwise follow the installation step.

### Installation
Install a Python version greater than or equal to 3.11 on your machine.

To install the required Python packages, run the following command in terminal:

```bash
pip install -r requirements.txt
```

### Usage
The images you want to calculate fractal dimensions for must be in the images folder. (Supported file types: jpg, png, tif, gif)
From the terminal, go to the folder where you extracted the project files. Then the project can be run simply with the following command:

```bash
python main.py
```

When the interface is running, simply click on the location you want to calculate fractal dimension.
The second click removes the previous calculation.
You can click on the location you want to calculate fractal dimension again.
Press q to exit the program.
