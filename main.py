import os
from app import create_app, db
from data_processing.load_ohio import load_ohio_excel_data
from app.models import WellData

app = create_app()

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', '20210309_2020.xls')

with app.app_context():
    db.create_all()

    if WellData.query.count() == 0:
        load_ohio_excel_data(file_path)

if __name__ == "__main__":
    app.run(port=8080)
