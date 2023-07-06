resource "google_storage_bucket" "frontend" {
  name            = "privacy-engineering-frontend"
  location        = "EUROPE-WEST3"
  force_destroy   = false
}

# TODO @christianstubbe: Refactor zip creation with GitHub Actions to automate npm run build
resource "google_storage_bucket_object" "frontend" {
  name   = "frontend/"
  bucket = google_storage_bucket.frontend.name
  source = "./../frontend/build/"
}

# TODO @christianstubbe: Refactor into Terraform State to prevent Error 409: This application already exists and cannot be re-created
# resource "google_app_engine_application" "app" {
#   project            = "tu-berlin-privacy-engineering"
#   location_id        = "EUROPE-WEST3"
# }
 
# TODO @christianstubbe: Solve on terraform destroy Error 400: The default service (module) cannot be deleted
resource "google_app_engine_standard_app_version" "app_v1" {
  version_id         = "v1"
  service            = "default"
  runtime            = "nodejs18"

  deployment {
    zip {
      source_url = "https://storage.googleapis.com/${google_storage_bucket.frontend.name}/${google_storage_bucket_object.frontend.name}"
    }
  }

  entrypoint {
    shell = ""
  }

  handlers {
    url_regex                   = "/(.*)"
    redirect_http_response_code = "REDIRECT_HTTP_RESPONSE_CODE_301"
    security_level              = "SECURE_ALWAYS"
    static_files {
      path              = "build/\\1"
      upload_path_regex = "build/.*"
    }
  }

  handlers {
    url_regex                   = ".*"
    redirect_http_response_code = "REDIRECT_HTTP_RESPONSE_CODE_301"
    security_level              = "SECURE_ALWAYS"
    script {
      script_path = "auto"
    }
  }
 
  delete_service_on_destroy = false
}
