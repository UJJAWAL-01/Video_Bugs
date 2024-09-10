# Pre_Imaging_API

## Description

**Pre_Imaging_API** is a tool designed for performing pre-imaging tasks on datasets. It is intended to streamline the data preparation process before it is fed into machine learning or computer vision models.

## Features

- Load and preprocess image datasets.
- Resize images and perform normalization.
- Easy integration into existing machine learning pipelines.
- Flexible configuration for different imaging tasks.

## Requirements

- Python 3.8 or higher
- Required Python packages (can be installed via `requirements.txt`):
  - Flask
  = Flask-PyMongo
  - pymongo
  - dnspython


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Harshuthoke/API.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd API
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## MongoDB Configuration

To change the MongoDB URL, modify the `MONGO_URI` variable in the configuration file (usually found in `config.py` or similar file):

```python
MONGO_URI = "your_mongodb_url_here"
```

Make sure to update this with your MongoDB connection string.

## Usage

1. Import the necessary modules from the package in your Python project.
2. Set up configuration parameters for image preprocessing.
3. Call the appropriate functions to start preprocessing.

Example:

```python
from pre_imaging_api import ImagePreprocessor

# Initialize the image preprocessor
processor = ImagePreprocessor()

# Preprocess your dataset
processed_images = processor.preprocess_images(image_folder='path_to_images', output_size=(128, 128))
```

## File Structure

- **pre_imaging_api/**: Core API for pre-imaging tasks.
- **requirements.txt**: List of required Python libraries.
- **example_usage.py**: Example script demonstrating the usage of the API.
