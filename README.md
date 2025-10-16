# Fractal Box Counter
This repository contains a Python script for performing single click fractal box counting on medical images. It can be used for image analysis and fractal dimension calculation in dental research.
Download latest version [here](https://github.com/semruktech/fractal-box-counter/releases/download/v0.2.0/FractalBoxCounter.zip).

### Citations
- [23/08/2025] Single-click automated fractal analysis for dental radiographs: a comparative evaluation with classic ImageJ method DOI:[https://doi.org/10.1186/s12903-025-05932-4](https://doi.org/10.1186/s12903-025-05932-4).

```bibtex
@article{Balel_Sagtas_2025,
  author       = {Balel, Yunus and Sağtaş, Kaan},
  title        = {Single-click automated fractal analysis for dental radiographs: a comparative evaluation with classic ImageJ method},
  journal      = {BMC Oral Health},
  volume       = {25},
  number       = {1360},
  year         = {2025},
  doi          = {10.1186/s12903-025-05932-4},
  url          = {https://link.springer.com/article/10.1186/s12903-025-05932-4}
}
```

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
The images you want to calculate fractal dimensions for must be in the images (Supported file types: jpg, png, tif, gif) folder.
From the terminal, go to the folder where you extracted the project files. Then the project can be run simply with the following command:

```bash
python main.py
```

When the interface is running: 
- Simply click on the location you want to calculate fractal dimension.
- The second click removes the previous calculation.
- You can click on the location you want to calculate fractal dimension again.
- Press q to exit the program.
