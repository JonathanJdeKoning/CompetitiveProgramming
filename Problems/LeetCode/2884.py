import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(employees)):
        employees["salary"][i] *=2
    return employees
