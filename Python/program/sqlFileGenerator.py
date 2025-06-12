def write_stage_files(templates):
    for business_key, model in templates:
        output_path = f"../../DBT/models/staging_automateDV/{business_key.lower()}_stage.sql"
        with open (output_path, "w") as f:
            f.write(model)

def write_hub_files(templates):
    for business_key, model in templates:
        output_path = f"../../DBT/models/hubs_automateDV/hub_{business_key.lower()}.sql"
        with open (output_path, "w") as f:
            f.write(model)