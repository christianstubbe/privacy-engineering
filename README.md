
# P3-Toolbox
The P3-Toolbox (Purpose-Based Privacy-Preserving Toolbox) enforces purpose-based access control in cloud-native applications. It is created as part of the module "Privacy Engineering" by Dr. Frank Pallas at Technische Universität Berlin. 

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
[![Terraform](https://github.com/christianstubbe/usability-engineering/actions/workflows/terraform.yml/badge.svg)](https://github.com/christianstubbe/usability-engineering/actions/workflows/terraform.yml)

## Table of Contents

  - [Deployment](#deployment)
  - [Local Installation](#local-installation)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Deployment

The toolbox is designed to be deployed on a event-driven serverless execution environment e.g. Google Cloud Functions. To simplify deployment in Google Cloud, there is a terraform configuration in the terraform folder.

1. Edit ```terraform/main.tf``` and enter your project id, default zone and default region. 
2. in the ```terraform/``` folder run ```terraform init``` 
3. Run  ```terraform plan``` to create an execution plan to preview the changes that Terraform makes to your infrastructure. 
4. Run ```terraform apply``` to execute the actions proposed in the terraform plan.

If you do not want to use terraform to deploy the toolbox, you can run it in any python 3.11 runtime environment. The requirements are listed in ```toolbox/src/requirements.txt```

## Local Installation

### Prerequisites

- Google Cloud CLI
- Terraform
- Serverless CLI

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Setup

```sh
pip install -r requirements.txt
```

## Features
The toolbox currently supports the following features. To create a feature request, go to the list of issues and click on the “New issue” button on the right. 
- Policy decision making
- Purpose policies
	- Creation
	- Deletion
	- Modifiction
	- Hierarchical organisation (purpose trees)
	- Purpose limitation and exception
- Data Transformation
	- Image erosion
	- Image background removal
	- Image downsizing
	- Image blurring
	- Image grayscale


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- Dr. Frank Pallas, Technische Universität Berlin
