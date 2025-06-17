from excel_reader import read_excel, get_fields
from stage import Stage
from satellite import Satellite
from link import Link
from hub import Hub

def main():
    excelDataframe = read_excel()
    valueDicts = get_fields(excelDataframe)
    for dict in valueDicts:
        stageObject = Stage(
            dict.get("source_model"),
            dict.get("src_source"),
            dict.get("src_nk"),
            dict.get("hashdiff_columns")
        )
        stageObject.write_stage_model(stageObject.edit_stage_template())

        satelliteObject = Satellite(
            dict.get("src_nk"),
            dict.get("src_nk").lower() + "_stage",
            dict.get("src_nk") + "_HK",
            dict.get("src_nk") + "_HASHDIFF",
            dict.get("hashdiff_columns"),
            dict.get("src_eff")
        )
        satelliteObject.write_sat_model(satelliteObject.edit_sat_template())

        linkObject = Link(
            dict.get("src_nk").lower() + "_stage",
            dict.get("src_nk") + "_" + "LINKSOURCE2" + "_HK"
        )
        linkObject.write_link_model(linkObject.edit_link_template())

        hubObject = Hub(
            dict.get("src_nk").lower().join("_stage"),
            dict.get("src_nk") + "_HK",
            dict.get("src_nk")
        )
        hubObject.write_hub_model(hubObject.edit_hub_template())

if __name__ == "__main__":
    main()