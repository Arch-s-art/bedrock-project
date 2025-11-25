variable "knowledge_base_name" {
  type = string
}
variable "knowledge_base_description" {
  type = string
}
variable "vpc_id" {
  type = string
}
variable "private_subnet_ids" {
  type = list(string)
}
variable "public_subnet_ids" {
  type = list(string)
}
variable "s3_bucket_name" {
  type = string
}
variable "s3_bucket_arn" {
  type = string
}
variable "aurora_arn" {
  type = string
}
variable "aurora_db_name" {
  type = string
}
variable "aurora_endpoint" {
  type = string
}
variable "aurora_table_name" {
  type = string
}
variable "aurora_primary_key_field" {
  type = string
}
variable "aurora_metadata_field" {
  type = string
}
variable "aurora_text_field" {
  type = string
}
variable "aurora_verctor_field" {
  type = string
}
variable "aurora_username" {
  type = string
}
variable "aurora_secret_arn" {
  type = string
}
variable "parsing_strategy" {
  type = string
}
variable "chunking_strategy" {
  type = string
}
variable "chunk_size" {
  type = number
}
variable "region" { type = string }
