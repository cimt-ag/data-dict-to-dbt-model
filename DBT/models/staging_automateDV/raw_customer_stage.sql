{{ config(materialized='view') }}

{%- set yaml_metadata -%}
source_model:
    raw_customer: 'raw_customer'
derived_columns:
    SOURCE: "!1"
    LOAD_DATETIME: "CRM_DATA_INGESTION_TIME"
    EFFEKTIVE_FROM: "BOOKING_DATE"
    START_DATE: "BOOKING_DATE"
    END_DATE: "TO_DATE('9999-12-31')"
hashed_columns:
    CUSTOMER_HK: "CUSTOMER_ID"
    NATION_HK: "NATION_ID"
    CUSTOMER_NATION_HK:
      - "CUSTOMER_ID"
      - "NATION_ID"
    CUSTOMER_HASHDIFF:
      is_hashdiff: true
      columns:
        - "CUSTOMER_NAME"
        - "CUSTOMER_ID"
        - "CUSTOMER_PHONE"
        - "CUSTOMER_BIRTHDAY"
{%- endset -%}

{% set metadata_dict = fromyaml(yaml_metadata) %}

{{ automate_dv.stage(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}