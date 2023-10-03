from flask import Flask, render_template, redirect, url_for
from flask import request, Response, jsonify
import mongo as dbase
from product import Product

app = Flask(__name__)
db=dbase.dbconnection()

@app.route("/")
def home():
    product =db['PRODUCTOS']
    producsReceived = product.find()

    return render_template('index.html', products=producsReceived)


@app.route("/lectura")
def lectura():
   # resul=db_client.find_one()
    #print(resul)
    return "f<p>SEG</p>"

#Method Post

@app.route('/products', methods=['POST'])
def addProduct():
    products = db['PRODUCTOS']
    Modelo = request.form['model']
    descripcion = request.form['description']
    costo = request.form['valor']

    if Modelo and descripcion and costo:
        product = Product(Modelo, descripcion, costo)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'Modelo': Modelo,
            "Description": descripcion,
            "valor": costo
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)