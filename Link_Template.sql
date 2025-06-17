{{ config(materialized='incremental') }}

{{%- set source_model = "{source_model}" -%}}
{{%- set src_pk = "{src_pk}" -%}}
{{%- set src_fk = "{src_fk}" -%}}
{{%- set src_ldts = "{src_ldts}" -%}}
{{%- set src_source = "{src_source}" -%}}

{{ automate_dv.link(src_pk=src_pk, src_fk=src_fk, src_ldts=src_ldts,
                   src_source=src_source, source_model=source_model) }}