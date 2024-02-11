from flask import Flask, request
from config import API_KEY, API_SECRET, PASSWORD
from binance.cm_futures import CMFutures
from binance.um_futures import UMFutures

app = Flask(__name__)

UM_futures_client = UMFutures()



UM_futures_client = UMFutures(key= API_KEY, 
                              secret= API_SECRET)




@app.route("/alert", methods=['POST'])

def alerta():
    msg = request.json
    if msg['password'] != PASSWORD:
        return { 'code': 'error',
                'message': 'User not authorized'
        }
    print(msg)

   
 

    response = UM_futures_client.new_order( msg['symbol'], msg['side']  ,msg['type'] ,msg['quantity'] ,msg['timestamp'] )
    print(response)   
    
    return {
        'code' : 'Success',
        'msg': msg  


    }



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)





 


 