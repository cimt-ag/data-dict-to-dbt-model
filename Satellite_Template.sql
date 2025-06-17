{{{{ config(materialized='{materialization}') }}}}

{{%- set yaml_metadata -%}}
source_model: "{source_model}"
src_pk: "{src_pk}"
src_hashdiff:
    source_column: "{src_column}"
    alias: "{alias}"
src_payload:
{payload_columns}
src_eff: "{src_eff}"
src_ldts: "{src_ldts}"
src_source: "{src_source}"

{{%- endset -%}}

{{% set metadata_dict = fromyaml(yaml_metadata) %}}

{{{{ automate_dv.sat(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}}}