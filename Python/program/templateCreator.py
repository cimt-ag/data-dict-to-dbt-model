def create_stage_templates(stageObjects):
    stageTemplates = []
    for stage in stageObjects:
        stageTemplate = stage.edit_stage_template()
        stageTemplates.append((stage.business_key, stageTemplate))
    return stageTemplates

def create_hub_templates(hubObjects):
    hubTemplates = []
    for hub in hubObjects:
        hubTemplate = hub.edit_hub_template()
        hubTemplates.append((hub.business_key, hubTemplate))
    return hubTemplates