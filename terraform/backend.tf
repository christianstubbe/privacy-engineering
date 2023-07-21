terraform {
 backend "gcs" {
   bucket  = "terraform-state-bucket-tfstate"
   prefix  = "terraform/state"
 }
}

resource "google_storage_bucket" "default" {
  name          = "terraform-state-bucket-tfstate"
  force_destroy = false
  location      = "EUROPE-WEST3"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}