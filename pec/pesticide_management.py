import mysql.connector

def apply_pesticide(crop_name, total_acres, pesticide_type):
    try:
        # Establishing connection to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Siddha@2234",
            database="agribot"
        )
        cursor = conn.cursor()

        # Query to fetch cost per acre, brand, and pest name
        if pesticide_type=="insecticide":
            query = """
                select  insecticide_name , insecticide_brand ,
                insecticide_price_per_acre , insecticide_price_per_gallon 
                from pesticide where
                crop_name =  %s
            """
        elif pesticide_type=="herbicide":
            query = """
                select herbicide_name , herbicide_brand ,
                herbicide_price_per_acre , herbicide_price_per_gallon 
                from pesticide where
                crop_name =  %s
            """
        elif pesticide_type=="fungicide":
            query = """
                select fungicide_name , fungicide_brand , 
                fungicide_price_per_acre , fungicide_price_per_gallon 
                from pesticide where
                crop_name =  %s 
            """
        else:
            pass

        # Executing the query with the provided crop name and pesticide type
        cursor.execute(query, (crop_name,))

        # Fetching the result
        result = cursor.fetchone()
        
        # Calculating total price and total gallons
        if result:
            pest_name, pest_brand, price_per_acre, price_per_gallon = result
            total_price = total_acres * price_per_acre
            total_gallons = total_price / price_per_gallon
            return pest_name, pest_brand, total_price, total_gallons
        else:
            return None

        # Closing cursor and connection
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        return None
    
def get_prices(crop_name):
    try:
        # Establishing connection to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Siddha@2234",
            database="agribot"
        )
        cursor = conn.cursor()
        query = "select crop_price,seed_price from crop_prices where crop_name = %s"
        cursor.execute(query, (crop_name,))
        result = cursor.fetchone()
        crop_price , seed_price = result
        return crop_price,seed_price
        
        cursor.close()
        conn.close()
    
    except mysql.connector.Error as e:
        return None
    
r = get_prices('Potato')
print(r)