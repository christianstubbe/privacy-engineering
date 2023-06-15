terraform {
    required_providers {
        google = {
            source  = "hashicorp/google"
            version = ">= 4.34.0"
        }
    }
}

provider "google" {
    project = "tu-berlin-privacy-engineering"
    region  = "eu-west3"
    zone    = "eu-west1-a"
}

resource "google_compute_network" "vpc_network" {
    name = "terraform-network"
}