from flask import Flask,request, jsonify
app=Flask(__name__)

@app.route('/getProducts',methods=['GET'])
def get_products():
    
    return "Hello, how are you"

if __name__=="__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
