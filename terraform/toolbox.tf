
resource "google_storage_bucket" "toolbox" {
  name            = "privacy-engineering-toolbox"
  location        = "EUROPE-WEST3"
  force_destroy   = false
}

# TODO @christianstubbe: Add hashsum to zip to enable Cloud Function Redeployment on source code change
data "archive_file" "toolbox" {
  type            = "zip"
  output_path     = "/tmp/toolbox.zip"
  source_dir      = "./../src/"
}

resource "google_storage_bucket_object" "toolbox" {
  name            = "toolbox.zip"
  bucket          = google_storage_bucket.toolbox.name
  source          = data.archive_file.toolbox.output_path 
}

resource "google_cloudfunctions2_function" "toolbox" {
  name            = "privacy-engineering-toolbox"
  location        = "europe-west1"

  build_config {
    runtime       = "python311"
    entry_point   = "hello_world"
    source {
      storage_source {
        bucket = google_storage_bucket.toolbox.name
        object = google_storage_bucket_object.toolbox.name
      }
    }
  }
}
