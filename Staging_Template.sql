{{ config(materialized='view') }}

{%- set yaml_metadata -%}
source_model:
    raw_customer: 'raw_customer' -- Needs to be adjusted to actual source
derived_columns:
    META_REC_SRC: "" -- source/system + . + table/file
    META_LOAD_DTS: "TIMESTAMP()" -- TIMESTAMP FUNCTION
    META_JOB_INSTANCE_ID: "-1"
    META_ENCRYPTIONKEY_INDEX: "0"
hashed_columns:
    {{target_field_name}}_HK: "" --target field name -> alternative name -> field name in source system
    -- Eventuell, falls mehrere gefunden werden: --
    {{target_table_name}}_HK: -- name unter vorbehalt
        - {{target_field_name_value1}}
        - {{target_field_name_value2}}
    FIELD_HASHDIFF:
      is_hashdiff: true
      columns:
        - "<>"
{%- endset -%}

{% set metadata_dict = fromyaml(yaml_metadata) %}

{{ automate_dv.stage(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}