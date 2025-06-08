# Ecommerce Analytics with dbt + PostgreSQL

## Overview
Transform raw e-commerce data into analytics-ready tables using dbt's modular SQL and medallion architecture (staging → intermediate → marts).

## Getting Started

### Requirements
- PostgreSQL
- dbt-postgres (`pip install dbt-postgres`)

### Setup

1. Create database:
   ```bash
   createdb ecommerce
   ```

2. Load raw data:
   ```bash
   psql ecommerce < data/raw_data.sql
   ```

3. Configure `~/.dbt/profiles.yml`:
   ```yaml
   ecommerce_analytics:
     target: dev
     outputs:
       dev:
         type: postgres
         host: localhost
         user: your_user
         password: your_password
         dbname: ecommerce
         schema: public
         threads: 1
   ```

4. Run dbt:
   ```bash
   dbt run
   dbt test
   dbt docs generate && dbt docs serve
   ```

## Project Structure

- `staging/`: cleans raw data
- `intermediate/`: joins + logic
- `marts/`: final fact tables for analytics
