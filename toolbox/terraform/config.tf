terraform {
  cloud {
    organization = "peng-pbac-toolbox"

    workspaces {
      name = "peng-pbac-toolbox"
    }
  }

  required_providers {
        google = {
            source  = "hashicorp/google"
            version = ">= 4.34.0"
        }
    }
}