from flask import Flask
from flask_cors import CORS
from monitor import SystemMonitor

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    system_info = SystemMonitor()

    mem = system_info.get_mem()
    disk = system_info.get_disk()
    net = system_info.get_net()
    cpu = system_info.get_cpu()
    gpu = system_info.get_gpu()
    user_info = system_info.get_user_info()
    
    return {'mem': mem, 'disk': disk, 'net': net, 'cpu': cpu, 'gpu': gpu, 'user_info': user_info}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)