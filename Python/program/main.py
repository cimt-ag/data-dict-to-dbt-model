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

        satelliteObject = Satellite(
            dict.get("src_nk"),
            dict.get("src_nk").lower() + "_stage",
            dict.get("src_nk") + "_HK",
            dict.get("src_nk") + "_HASHDIFF",
            dict.get("hashdiff_columns"),
            dict.get("src_eff")
        )

        linkObject = Link(
            dict.get("src_nk").lower() + "_stage",
            dict.get("src_nk") + "_" + "LINKSOURCE2" + "_HK"
        )

        hubObject = Hub(
            dict.get("src_nk").lower() + "_stage",
            dict.get("src_nk") + "_HK",
            dict.get("src_nk")
        )

        stageObject.write_model(stageObject.edit_template())
        satelliteObject.write_model(satelliteObject.edit_template())
        linkObject.write_model(linkObject.edit_template())
        hubObject.write_model(hubObject.edit_template())

if __name__ == "__main__":
    main()