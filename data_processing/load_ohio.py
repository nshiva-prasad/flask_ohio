import pandas as pd
from app.models import WellData, db

def load_ohio_excel_data(file_path):
    df = pd.read_excel(file_path)

    annual_data = df.groupby('API WELL  NUMBER').agg({
        'OIL': 'sum',
        'GAS': 'sum',
        'BRINE': 'sum'
    }).reset_index()

    for _, row in annual_data.iterrows():
        well = WellData(
            api_well_number=str(row['API WELL  NUMBER']),
            oil=str(row['OIL']),
            gas=str(row['GAS']),
            brine=str(row['BRINE'])
        )
        db.session.add(well)
    db.session.commit()
