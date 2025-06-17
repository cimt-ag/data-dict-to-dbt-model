{{{{ config(materialized='view') }}}}

{{%- set yaml_metadata -%}}
source_model: "{source_model}"
src_pk: "{src_pk}"
src_hashdiff:
    source_column: "{src_nk}_HASHDIFF"
src_payload:
    - "{}"
    - "{}"
    - "{}"
src_eff: "{src_effective_from}"
src_ldts: "META_LOAD_DTS"
src_source: "META_REC_SRC"

{{%- endset -%}}

{{% set metadata_dict = fromyaml(yaml_metadata) %}}

{{{{ automate_dv.sat(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}}}