from flask import Blueprint, jsonify, request

from .models import WellData

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_well_data():
    well_number = request.args.get('well')
    if not well_number:
        return jsonify({'error': 'API WELL NUMBER is required'}), 400

    well = WellData.query.filter_by(api_well_number=well_number).first()

    if well:
        return jsonify({
            'oil': well.oil,
            'gas': well.gas,
            'brine': well.brine
        }), 200
    else:
        return jsonify({'error': f'Well data with "{well_number}" not found'}), 404
