from excel_reader import read_excel, get_fields
from hub import Hub

def main():
    excelDataframe = read_excel()
    valueDicts = get_fields(excelDataframe)
    for dict in valueDicts:
        hubObject = Hub(
            dict.get("source_model"),
            dict.get("src_pk"),
            dict.get("src_nk"),
            dict.get("src_ldts"),
            dict.get("src_source")
        )
        hubObject.write_hub_model(hubObject.edit_hub_template())

if __name__ == "__main__":
    main()