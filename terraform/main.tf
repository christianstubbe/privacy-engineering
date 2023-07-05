provider "google" {
    project     = "tu-berlin-privacy-engineering"
    region      = "europe-west3"
    zone        = "europe-west3-a"
}

# TODO @christianstubbe: Enable App Engine APIs
# TODO @christianstubbe: Enable Cloud Function APIs
# TODO @christianstubbe: Add IAM with project group and lecturer
# TODO @christianstubbe: Refactor main.tf with variable usage to enforce uniform regions