stage_template_str = """
{{ config(materialized='view') }}

{%- set yaml_metadata -%}
source_model:
    raw_customer: 'raw_customer'
derived_columns:
    META_REC_SRC: "<-- meta_rec_src -->"
    META_LOAD_DTS: "{{ dbt.current_timestamp() }}"
    META_JOB_INSTANCE_ID: "<-- meta_job_instance_id -->"
    META_ENCRYPTIONKEY_INDEX: "<-- meta_encryptionkey_index -->"
hashed_columns:
    <-- business_key -->_HK: "<-- business_key -->"
{%- endset -%}

{% set metadata_dict = fromyaml(yaml_metadata) %}

{{ automate_dv.stage(include_source_columns=true,
                     source_model=metadata_dict['source_model'],
                     derived_columns=metadata_dict['derived_columns'],
                     null_columns=none,
                     hashed_columns=metadata_dict['hashed_columns'],
                     ranked_columns=none) }}
"""

hub_template_str = """
{{ config(materialized='incremental') }}

{%- set source_model = "raw_customer_stage" -%}
{%- set src_pk = "<-- business_key -->_HK" -%}
{%- set src_nk = "<-- business_key -->" -%}
{%- set src_ldts = "META_LOAD_DTS" -%}
{%- set src_source = "META_REC_SRC" -%}

{{ automate_dv.hub(src_pk=src_pk, src_nk=src_nk, src_ldts=src_ldts,
                   src_source=src_source, source_model=source_model) }}
"""

def create_stage_templates(stageObjects):
    stageTemplates = []
    for stage in stageObjects:
        stageTemplate = edit_stage_template(stage)
        stageTemplates.append((stage.business_key, stageTemplate))
    return stageTemplates

def edit_stage_template(stage):
    editedStageTemplate = stage_template_str
    editedStageTemplate = editedStageTemplate.replace("<-- meta_rec_src -->", str(stage.meta_rec_src))
    editedStageTemplate = editedStageTemplate.replace("<-- meta_job_instance_id -->", str(stage.meta_job_instance_id))
    editedStageTemplate = editedStageTemplate.replace("<-- meta_encryptionkey_index -->", str(stage.meta_encryptionkey_index))
    editedStageTemplate = editedStageTemplate.replace("<-- business_key -->", str(stage.business_key))
    return editedStageTemplate

def create_hub_templates(hubObjects):
    hubTemplates = []
    for hub in hubObjects:
        hubTemplate = edit_hub_template(hub)
        hubTemplates.append((hub.src_nk, hubTemplate))
    return hubTemplates

def edit_hub_template(hub):
    editedHubTemplate = hub_template_str
    editedHubTemplate = editedHubTemplate.replace("<-- business_key -->", str(hub.src_nk))
    return editedHubTemplate