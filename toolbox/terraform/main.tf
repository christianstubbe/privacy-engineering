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
    region  = "europe-west1"
    zone    = "europe-west1-a"
}

resource "google_storage_bucket" "default" {
  name                        = "privacy-engineering-toolbox-source"
  location                    = "EUROPE-WEST1"
  force_destroy               = false
}

data "archive_file" "default" {
  type        = "zip"
  output_path = "/tmp/function-source.zip"
  source_dir  = "../src/"
}

resource "google_storage_bucket_object" "object" {
  name   = "toolbox-source.zip"
  bucket = google_storage_bucket.default.name
  source = data.archive_file.default.output_path # Add path to the zipped function source code
}

resource "google_cloudfunctions2_function" "default" {
  name        = "privacy-engineering-toolbox"
  location    = "europe-west1"

  build_config {
    runtime     = "python311"
    entry_point = "hello_world"
    source {
      storage_source {
        bucket = google_storage_bucket.default.name
        object = google_storage_bucket_object.object.name
      }
    }
  }
}