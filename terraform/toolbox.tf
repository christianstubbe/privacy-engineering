resource "google_storage_bucket" "toolbox" {
  name            = "privacy-engineering-toolbox"
  location        = "EUROPE-WEST3"
  force_destroy   = true
}

data "archive_file" "toolbox" {
  type            = "zip"
  output_path     = "/tmp/toolbox.zip"
  source_dir      = "./../toolbox/src/"
}

resource "google_storage_bucket_object" "toolbox" {
  name            = "toolbox.zip"
  bucket          = google_storage_bucket.toolbox.name
  source          = data.archive_file.toolbox.output_path
}

resource "google_cloudfunctions2_function" "toolbox" {
  name            = "privacy-engineering-toolbox"
  location        = "europe-west1"

  service_config {
    secret_environment_variables {
      key = "DB_NAME"
      secret = "DB_NAME"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "DB_PASSWORD"
      secret = "DB_PASSWORD"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "DB_URL"
      secret = "DB_URL"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "DB_USERNAME"
      secret = "DB_USERNAME"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "GCP_PROJECT_NAME"
      secret = "GCP_PROJECT_NAME"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "GCP_PROJECT_NB"
      secret = "GCP_PROJECT_NB"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "GOOGLE_APPLICATION_CREDENTIALS"
      secret = "GOOGLE_APPLICATION_CREDENTIALS"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
    secret_environment_variables {
      key = "JWT_SECRET_TOKEN"
      secret = "JWT_SECRET_TOKEN"
      version = "latest"
      project_id = "tu-berlin-privacy-engineering"
    }
  }

  build_config {
    runtime       = "python311"
    entry_point   = "entry_point"
    source {
      storage_source {
        bucket = google_storage_bucket.toolbox.name
        object = google_storage_bucket_object.toolbox.name
      }
    }
  }
}
