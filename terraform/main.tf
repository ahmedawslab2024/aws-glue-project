provider "aws" {
  region = "eu-west-1"
}

resource "aws_s3_bucket" "data_lake" {
  bucket = "your-bucket"
}

resource "aws_glue_job" "ingest" {
  name     = "job_ingest"
  role_arn = aws_iam_role.glue_role.arn
  command {
    name            = "glueetl"
    script_location = "s3://your-bucket/scripts/job_ingest.py"
    python_version  = "3"
  }
}

resource "aws_glue_job" "transform" {
  name     = "job_transform"
  role_arn = aws_iam_role.glue_role.arn
  command {
    name            = "glueetl"
    script_location = "s3://your-bucket/scripts/job_transform.py"
    python_version  = "3"
  }
}