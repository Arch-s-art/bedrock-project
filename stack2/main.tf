provider "aws" {
  region = "us-west-2"
}

module "bedrock_kb" {
  source = "../modules/bedrock_kb"

  knowledge_base_name        = var.knowledge_base_name
  knowledge_base_description = var.knowledge_base_description

  aurora_arn               = var.aurora_arn
  aurora_db_name           = var.aurora_db_name
  aurora_endpoint          = var.aurora_endpoint
  aurora_table_name        = var.aurora_table_name
  aurora_primary_key_field = var.aurora_primary_key_field
  aurora_metadata_field    = var.aurora_metadata_field
  aurora_text_field        = var.aurora_text_field
  aurora_verctor_field     = var.aurora_verctor_field
  aurora_username          = var.aurora_username
  aurora_secret_arn        = var.aurora_secret_arn
  s3_bucket_arn            = var.s3_bucket_arn

  #parsing_strategy         = var.parsing_strategy
  #chunking_strategy        = var.chunking_strategy
  #chunk_size               = var.chunk_size
}
