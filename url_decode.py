import pandas as pd
import urllib.parse
import json

# Simulate a DataFrame with the necessary columns
data = {
    'customer_id': ['cust123'],
    'orderid': ['order789'],
    'query_map': ["%7B%220%22%3A%7B%22id%22%3A%2211SVT4FW5PO3%22%2C%22fsc%22%3A0%2C%22dp%22%3A31.99%2C%22we%22%3A%22%22%2C%22ut%22%3A%22EACH%22%2C%22us%22%3A%221055383240%22%2C%22nm%22%3A%22Nonstick%20Bakeware%20Set%2C%20KITESSENSU%207-Piece%20Baking%20Pans%20Sets%20with%20Round%2FSquare%20Cake%20Pan%2C%20Cookie%20Sheet%20Sets%2C%20Roast%20Cooling%20Rack%2C%20Carbon%20Steel%20Bake-Black%22%2C%22av%22%3A1%2C%22dsc%22%3A%7B%22nm%22%3A%22promoDiscount%22%2C%22oid%22%3A%22AC587C451A244AA69B2B8D630FC1E82E%22%7D%2C%22qu%22%3A1%2C%22su%22%3A%7B%22ss%22%3A0%2C%22se%22%3A0%2C%22fv%22%3A0%2C%22fu%22%3A%22%22%7D%2C%22sa%22%3A0%2C%22li%22%3A%22%22%2C%22lt%22%3A%22%22%2C%22ipr%22%3A0%2C%22hrd%22%3A0%2C%22pit%22%3A%22%22%2C%22fl%22%3A%7B%22dd%22%3A%222024-02-15%22%2C%22dt%22%3A%222024-02-15T22%3A59%3A00Z%22%2C%22id%22%3A%22FCGroup_7CB8BE91AB334F59ADBB4FEF24ED3E62WFS%22%2C%22nm%22%3A%22Shipping%22%2C%22fr%22%3A%22FC%22%2C%22pp%22%3A0%2C%22si%22%3A%22%22%7D%2C%22fa%22%3A%22%22%2C%22ss%22%3A%22%22%2C%22se%22%3A%7B%22nm%22%3A%22Hangzhou%20bengda%20keji%20youxiangongsi%22%2C%22id%22%3A%227CB8BE91AB334F59ADBB4FEF24ED3E62%22%2C%22sb%22%3A1%2C%22st%22%3A%22WFS%22%7D%2C%22po%22%3A0%2C%22pca%22%3A0%2C%22pcp%22%3A0%2C%22pcs%22%3A%22%22%2C%22mn%22%3A%22Shipping%22%2C%22iz%22%3A0%2C%22br%22%3A%22KITESSENSU%22%2C%22cn%22%3A%22Home%20Page%2FHome%2FKitchen%20%26%20Dining%2FBakeware%2FShop%20Bakeware%22%2C%22ci%22%3A%220%3A4044%3A623679%3A8455465%3A4081038%22%2C%22im%22%3A%7B%7D%2C%22csr%22%3A0%2C%22pa%22%3A0%2C%22ad%22%3A0%2C%22aa%22%3A0%7D%2C%221%22%3A%7B%22id%22%3A%226JKCWE2PM613%22%2C%22fsc%22%3A0%2C%22dp%22%3A8%2C%22we%22%3A%22%22%2C%22ut%22%3A%22EACH%22%2C%22ps%22%3A2.73%2C%22us%22%3A%2249700702%22%2C%22nm%22%3A%22Whirlpool%20W10311524%20FreshFlow%20Refrigerator%20Air%20Filter%22%2C%22av%22%3A1%2C%22dsc%22%3A%7B%22nm%22%3A%22promoDiscount%22%2C%22oid%22%3A%22C2C7EF01297849BFAF56D53DD077A40E%22%7D%2C%22qu%22%3A1%2C%22su%22%3A%7B%22ss%22%3A0%2C%22se%22%3A0%2C%22fv%22%3A0%2C%22fu%22%3A%22%22%7D%2C%22sa%22%3A0%2C%22li%22%3A%22%22%2C%22lt%22%3A%22%22%2C%22ipr%22%3A0%2C%22hrd%22%3A0%2C%22pit%22%3A%22%22%2C%22fl%22%3A%7B%22dd%22%3A%222024-02-17%22%2C%22dt%22%3A%222024-02-17T20%3A00%3A00Z%22%2C%22id%22%3A%22FCGroup_DDD1F535743643ECB371F1C38BC5077EMARKETPLACE%22%2C%22nm%22%3A%22Shipping%22%2C%22fr%22%3A%22FC%22%2C%22pp%22%3A0%2C%22si%22%3A%22%22%7D%2C%22fa%22%3A%22%22%2C%22ss%22%3A%22%22%2C%22se%22%3A%7B%22nm%22%3A%22M7%20Ocean%22%2C%22id%22%3A%22DDD1F535743643ECB371F1C38BC5077E%22%2C%22sb%22%3A1%2C%22st%22%3A%223P%22%7D%2C%22po%22%3A0%2C%22pca%22%3A0%2C%22pcp%22%3A0%2C%22pcs%22%3A%22%22%2C%22mn%22%3A%22Shipping%22%2C%22iz%22%3A0%2C%22br%22%3A%22Whirlpool%22%2C%22cn%22%3A%22Home%20Page%2FHome%20Improvement%2FWater%20Purification%2FWater%20Filters%2FRefrigerator%20Water%20Filters%2FAll%20Refrigerator%20Water%20Filters%22%2C%22ci%22%3A%220%3A1072864%3A6610571%3A1231153%3A1230874%3A4505596%22%2C%22im%22%3A%7B%7D%2C%22csr%22%3A0%2C%22pa%22%3A0%2C%22ad%22%3A0%2C%22aa%22%3A0%7D%2C%222%22%3A%7B%22id%22%3A%224WYHHFJ6M1GX%22%2C%22fsc%22%3A0%2C%22dp%22%3A59.99%2C%22we%22%3A%22%22%2C%22ut%22%3A%22EACH%22%2C%22us%22%3A%221364351447%22%2C%22nm%22%3A%22Whirlpool%20Refrigerator%20Water%20Filter%201%20-%20WHR1RXD1%2C%20Single-Pack%2C%20Replace%20Every%206%20Months%2C%20Purple%22%2C%22av%22%3A1%2C%22dsc%22%3A%7B%22nm%22%3A%22promoDiscount%22%2C%22oid%22%3A%22DDC8CAA022A4478DB60676FE5EF99CA0%22%7D%2C%22qu%22%3A1%2C%22su%22%3A%7B%22ss%22%3A0%2C%22se%22%3A1%2C%22fv%22%3A0%2C%22fu%22%3A%22%22%7D%2C%22sa%22%3A0%2C%22li%22%3A%22%22%2C%22lt%22%3A%22%22%2C%22ipr%22%3A0%2C%22hrd%22%3A0%2C%22pit%22%3A%22%22%2C%22fl%22%3A%7B%22dd%22%3A%222024-02-14%22%2C%22dt%22%3A%222024-02-14T22%3A59%3A00Z%22%2C%22id%22%3A%22FCGroup_F55CDC31AB754BB68FE0B39041159D63WALMART%22%2C%22nm%22%3A%22Shipping%22%2C%22fr%22%3A%22FC%22%2C%22pp%22%3A0%2C%22si%22%3A%22%22%7D%2C%22fa%22%3A%22%22%2C%22ss%22%3A%22%22%2C%22se%22%3A%7B%22nm%22%3A%22Walmart.com%22%2C%22id%22%3A%22F55CDC31AB754BB68FE0B39041159D63%22%2C%22sb%22%3A0%2C%22st%22%3A%221P%22%7D%2C%22po%22%3A0%2C%22pca%22%3A0%2C%22pcp%22%3A0%2C%22pcs%22%3A%22%22%2C%22mn%22%3A%22Shipping%22%2C%22iz%22%3A0%2C%22br%22%3A%22Whirlpool%22%2C%22cn%22%3A%22Home%20Page%2FHome%20Improvement%2FWater%20Purification%2FWater%20Filters%2FRefrigerator%20Water%20Filters%2FWhirlpool%20Refrigerator%20Water%20Filters%22%2C%22ci%22%3A%220%3A1072864%3A6610571%3A1231153%3A1230874%3A1268487%22%2C%22im%22%3A%7B%7D%2C%22csr%22%3A0%2C%22pa%22%3A0%2C%22ad%22%3A0%2C%22aa%22%3A0%7D%2C%223%22%3A%7B%22id%22%3A%22729KHWRWM9EW%22%2C%22fsc%22%3A0%2C%22dp%22%3A64.99%2C%22we%22%3A%22%22%2C%22ut%22%3A%22EACH%22%2C%22ps%22%3A34.96%2C%22us%22%3A%2251678008%22%2C%22nm%22%3A%22Cuisinart%20Classic%20Forged%20Triple%20Rivet%2015-Piece%20Cutlery%20Set%20with%20Block%2C%20White%20and%20Stainless%2C%20C77WTR-15P%22%2C%22av%22%3A1%2C%22dsc%22%3A%7B%22nm%22%3A%22promoDiscount%22%2C%22oid%22%3A%22A710D2653CC645A1998CBB082B21CEDC%22%7D%2C%22qu%22%3A1%2C%22su%22%3A%7B%22ss%22%3A0%2C%22se%22%3A0%2C%22fv%22%3A0%2C%22fu%22%3A%22%22%7D%2C%22sa%22%3A0%2C%22li%22%3A%22%22%2C%22lt%22%3A%22%22%2C%22ipr%22%3A0%2C%22hrd%22%3A0%2C%22pit%22%3A%22%22%2C%22fl%22%3A%7B%22dd%22%3A%222024-02-14%22%2C%22dt%22%3A%222024-02-14T22%3A59%3A00Z%22%2C%22id%22%3A%22FCGroup_F55CDC31AB754BB68FE0B39041159D63WALMART%22%2C%22nm%22%3A%22Shipping%22%2C%22fr%22%3A%22FC%22%2C%22pp%22%3A0%2C%22si%22%3A%22%22%7D%2C%22fa%22%3A%22%22%2C%22ss%22%3A%22%22%2C%22se%22%3A%7B%22nm%22%3A%22Walmart.com%22%2C%22id%22%3A%22F55CDC31AB754BB68FE0B39041159D63%22%2C%22sb%22%3A0%2C%22st%22%3A%221P%22%7D%2C%22po%22%3A0%2C%22pca%22%3A0%2C%22pcp%22%3A0%2C%22pcs%22%3A%22%22%2C%22mn%22%3A%22Shipping%22%2C%22iz%22%3A0%2C%22br%22%3A%22Cuisinart%22%2C%22cn%22%3A%22Home%20Page%2FHome%2FFeatured%20Shops%2FPremium%20Kitchen%20Shop%2FCuisinart%22%2C%22ci%22%3A%220%3A4044%3A1225301%3A9409401%3A2436041%22%2C%22im%22%3A%7B%7D%2C%22csr%22%3A0%2C%22pa%22%3A0%2C%22ad%22%3A0%2C%22aa%22%3A0%7D%2C%22st%22%3A%7B%7D%7D"]
}
df = pd.DataFrame(data)

# Function to decode and extract id values
def extract_ids(encoded_str):
    try:
        # Decode the URL-encoded string
        decoded_str = urllib.parse.unquote(encoded_str)
        
        # Parse the JSON structure
        json_obj = json.loads(decoded_str)
        
        # Function to recursively search for 'id' keys in the JSON object
        def find_ids(obj, ids):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == 'id':
                        ids.append(value)
                    elif isinstance(value, (dict, list)):
                        find_ids(value, ids)
            elif isinstance(obj, list):
                for item in obj:
                    find_ids(item, ids)
            return ids
        
        # Initialize an empty list to store found ids
        ids = []
        # Recursively find 'id' values
        find_ids(json_obj, ids)
        
        return ids
    except Exception as e:
        return [f"Error: {str(e)}"]

# Apply the function to the 'query_map' column
df['extracted_ids'] = df['query_map'].apply(extract_ids)

# Display the DataFrame to verify the results
print(df[['customer_id', 'orderid', 'extracted_ids']])
