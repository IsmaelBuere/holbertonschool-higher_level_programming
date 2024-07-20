#!/usr/bin/python3
from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products = []
    error = None

    if source not in ['json', 'csv']:
        error = "Wrong source"
    else:
        try:
            if source == 'json':
                products_data = read_json_file('products.json')
            elif source == 'csv':
                products_data = read_csv_file('products.csv')
            
            if id_param:
                products = [product for product in products_data if str(product['id']) == id_param]
                if not products:
                    error = "Product not found"
            else:
                products = products_data

        except FileNotFoundError:
            error = f"File 'products.{source}' not found"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
