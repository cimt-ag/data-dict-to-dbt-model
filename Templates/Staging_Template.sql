{{{{ config(materialized='{materialization}') }}}}

{{%- set yaml_metadata -%}}
source_model:
    {source_model}: "{source_model}"
derived_columns:
    META_REC_SRC: "{src_source}"
    META_LOAD_DTS: "{src_ldts}"
    META_JOB_INSTANCE_ID: "{src_job_instance_id}"
    META_ENCRYPTIONKEY_INDEX: "{src_encryptionkey_index}"
hashed_columns:
    {src_nk}_HK: "{src_nk}"
    {src_nk}_HASHDIFF:
        is_hashdiff: true
        columns:
{hashdiff_columns}
{{%- endset -%}}

{{% set metadata_dict = fromyaml(yaml_metadata) %}}

{{{{ automate_dv.stage(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}}}