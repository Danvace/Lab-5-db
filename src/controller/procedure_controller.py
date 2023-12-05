from flask import Blueprint, jsonify, request
from sqlalchemy import text

from src import db

procedure_bp = Blueprint('procedure', __name__, url_prefix='/procedure')


@procedure_bp.get('/averagePrice')
def get_average_price():
    try:
        sql = text('CALL showAveragePrice()')
        result = db.session.execute(sql)

        results = result.fetchall()

        average_price = results[0][0]

        return jsonify({'average_price': average_price})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        db.session.close()


@procedure_bp.post('/insertOrderProductMapping')
def insert_order_product_mapping():
    try:
        order_id = request.json.get('order_id')
        product_id = request.json.get('product_id')

        sql = text('CALL InsertOrderProductMapping(:order_id, :product_id)')
        db.session.execute(sql, {'order_id': order_id, 'product_id': product_id})

        db.session.commit()

        return jsonify({'message': 'Order-Product Mapping inserted successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})

    finally:
        db.session.close()


@procedure_bp.post('/insertNonameRecords')
def insert_noname_records():
    try:
        product_id = request.json.get('product_id')

        sql = text('CALL InsertNonameRecords(:product_id)')
        db.session.execute(sql, {'product_id': product_id})

        db.session.commit()

        return jsonify({'message': 'Noname Records inserted successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})

    finally:
        db.session.close()


@procedure_bp.post('/reviewInsert')
def review_insert():
    try:
        product_id = request.json.get('product_id')
        response = request.json.get('response')

        sql = text('CALL review_insert(:product_id, :response)')
        db.session.execute(sql, {'product_id': product_id, 'response': response})

        db.session.commit()

        return jsonify({'message': 'Review inserted successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})

    finally:
        db.session.close()


@procedure_bp.post('/ProcCursor')
def proc_cursor():
    try:
        sql = text('CALL ProcCurso()')
        db.session.execute(sql)

        db.session.commit()

        return jsonify({'message': 'databases created successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)})
    finally:
        db.session.close()
