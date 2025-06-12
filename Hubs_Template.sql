{{ config(materialized='incremental') }}

{%- set source_model = "raw_customer_stage" -%}
{%- set src_pk = "{{target_field_name}}_HK" -%} -- Wird von dem Stage-Model generiert
{%- set src_nk = "{{target_field_name}}" -%}
{%- set src_ldts = "META_LOAD_DTS" -%}
{%- set src_source = "META_REC_SRC" -%}

{{ automate_dv.hub(src_pk=src_pk, src_nk=src_nk, src_ldts=src_ldts,
                   src_source=src_source, source_model=source_model) }}