import pandas as pd


def CSVtoJSON():
    with open('personas.json', "w") as file:
        file.write("")
        file.close()
        file = pd.DataFrame(pd.read_csv("personas.csv", sep=",", header=0, index_col=False))
        file.to_json('personas.json', orient="records", date_format="epoch", double_precision=10, force_ascii=True,
                     date_unit="ms", default_handler=None)
        print(file)
