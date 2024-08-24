from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Vineeth04!',
    'database': 'final_zomato_restaurants'
}

def get_db_connection():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        offset = (page - 1) * per_page

        # Get filter and search parameters
        restaurant_id = request.args.get('restaurant_id', type=int)
        country = request.args.get('country')
        avg_cost_min = request.args.get('avg_cost_min', type=float)
        avg_cost_max = request.args.get('avg_cost_max', type=float)
        cuisines = request.args.get('cuisines')
        search = request.args.get('search')

        # Build query with filters and search
        query = 'SELECT * FROM final_restaurants WHERE 1=1'
        params = []

        if restaurant_id is not None:
            query += ' AND `Restaurant ID` = %s'
            params.append(restaurant_id)
        if country:
            query += ' AND `Country Code` = %s'
            params.append(country)
        if avg_cost_min is not None:
            query += ' AND `Average Cost for two` >= %s'
            params.append(avg_cost_min)
        if avg_cost_max is not None:
            query += ' AND `Average Cost for two` <= %s'
            params.append(avg_cost_max)

        if cuisines:
            # Split the cuisines by comma
            cuisines_list = [c.strip() for c in cuisines.split(',')]
            # Add LIKE clauses for each cuisine
            for cuisine in cuisines_list:
                query += ' AND `Cuisines` LIKE %s'
                params.append(f'%{cuisine}%')

        if search:
            query += ' AND (`Restaurant Name` LIKE %s)'
            params.extend([f'%{search}%'])

        query += ' LIMIT %s OFFSET %s'
        params.extend([per_page, offset])

        cursor.execute(query, params)
        restaurants = cursor.fetchall()
        conn.close()

        if len(restaurants) == 1:
            # If exactly one restaurant matches, redirect to its detail page
            restaurant_id = restaurants[0]['Restaurant ID']
            return redirect(url_for('get_restaurant', restaurant_id=restaurant_id))

        # Otherwise, render the list of restaurants
        return render_template('restaurant_list.html', restaurants=restaurants, page=page, per_page=per_page, restaurant_id=restaurant_id, country=country, avg_cost_min=avg_cost_min, avg_cost_max=avg_cost_max, cuisines=cuisines, search=search)
    except Exception as e:
        app.logger.error('Error fetching restaurants: %s', e)
        return jsonify({'error': str(e)}), 500

@app.route('/restaurant', methods=['GET'])
@app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id=None):
    try:
        if restaurant_id is None:
            restaurant_id = request.args.get('restaurant_id', type=int)
            if not restaurant_id:
                return jsonify({'error': 'No restaurant ID provided'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM final_restaurants WHERE `Restaurant ID` = %s'
        cursor.execute(query, (restaurant_id,))
        restaurant = cursor.fetchone()
        conn.close()
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404
        return render_template('restaurant_detail.html', restaurant=restaurant)
    except Exception as e:
        app.logger.error('Error fetching restaurant details: %s', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
