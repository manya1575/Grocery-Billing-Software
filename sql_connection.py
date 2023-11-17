import mysql.connector as mydb
con=mydb.connect(user="root",passwd="admin123",host="localhost")
m=con.cursor()
m.execute("use gs")
#m.execute("select * from products")
m.execute("SELECT products.prod_id, products.name, products.uom_id,products.price_per_unit,uom.uom_name FROM products inner join uom on products.uom_id=uom.uom_id")
for row in m:
    print(row)
