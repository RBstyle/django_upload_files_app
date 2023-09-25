CREATE DATABASE upload_files;
CREATE USER upload_files_admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE upload_files TO upload_files_admin;
GRANT ALL ON ALL TABLES IN SCHEMA public to upload_files_admin;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to upload_files_admin;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to upload_files_admin;