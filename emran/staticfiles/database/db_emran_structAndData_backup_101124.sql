-- PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'emran','0001_initial','2024-11-10 08:19:15.132277');


CREATE TABLE IF NOT EXISTS "emran_certificationscoursestrainings" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cct_name" varchar(300) NOT NULL, "cct_description" text NULL, "cct_type" varchar(51) NOT NULL, "cct_offering_organisation" varchar(300) NOT NULL, "cct_funding_organisation" varchar(300) NULL, "cct_key_information" text NULL, "cct_hasexpire" bool NOT NULL, "cct_serial_no" varchar(10) NULL, "cct_start_date" date NOT NULL, "cct_end_date" date NULL, "cct_image" varchar(500) NULL, "cct_online_credential" varchar(1000) NULL);


CREATE TABLE IF NOT EXISTS "emran_honorsandawards" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "haw_title" varchar(300) NOT NULL, "haw_issuer_organisation" varchar(300) NOT NULL, "haw_associated_organisation" varchar(300) NULL, "haw_start_date" date NOT NULL, "haw_short_description" varchar(300) NOT NULL, "haw_description" text NULL);


CREATE TABLE IF NOT EXISTS "emran_languages" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "language_name" varchar(150) NOT NULL, "language_description" varchar(500) NOT NULL, "language_test_details" text NULL);


CREATE TABLE IF NOT EXISTS "emran_memberships" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "membership_name" varchar(150) NOT NULL, "membership_type" varchar(150) NOT NULL, "membership_organisation" varchar(500) NOT NULL, "membership_institution" varchar(500) NOT NULL, "membership_address" varchar(500) NOT NULL, "membership_hasexpire" bool NOT NULL, "membership_start_date" date NOT NULL, "membership_end_date" date NULL);


CREATE TABLE IF NOT EXISTS "emran_portfolios" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "portflio_platform_name" varchar(150) NOT NULL, "portflio_title" varchar(500) NOT NULL, "portflio_description" text NULL, "portflio_link" varchar(500) NOT NULL);


CREATE TABLE IF NOT EXISTS "emran_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_position" varchar(150) NOT NULL, "project_title" varchar(300) NOT NULL, "project_description" text NULL, "project_fund" varchar(300) NULL, "project_funding_organisation" varchar(500) NULL, "project_collaboration_organisation" varchar(500) NULL, "project_start_date" date NOT NULL, "project_end_date" date NULL, "project_image" varchar(500) NULL);


CREATE TABLE IF NOT EXISTS "emran_sessionsorevents" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "session_lead_name" varchar(150) NOT NULL, "session_lead_type" varchar(150) NOT NULL, "session_title" varchar(500) NOT NULL, "session_description" text NULL, "session_organisation" varchar(500) NOT NULL, "session_institution" varchar(500) NOT NULL, "session_address" varchar(500) NOT NULL, "session_start_date" date NOT NULL);


CREATE TABLE IF NOT EXISTS "emran_skillsandtools" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "sat_title" varchar(300) NOT NULL, "sat_short_description" varchar(600) NOT NULL, "sat_description" text NULL, "sat_skill_level" integer NOT NULL);


CREATE TABLE IF NOT EXISTS "emran_volunteering" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "volunteering_name" varchar(150) NOT NULL, "volunteering_involvement" varchar(150) NOT NULL, "volunteering_cause" varchar(150) NOT NULL, "volunteering_organisation" varchar(500) NOT NULL, "volunteering_start_date" date NOT NULL, "volunteering_end_date" date NULL, "volunteering_detail" text NULL, "volunteering_link" varchar(150) NOT NULL);

DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',1);

COMMIT;
