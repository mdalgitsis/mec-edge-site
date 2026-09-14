import collectd
from websocket import create_connection
import json
import threading
import ue_utils as utils


ue_list = []

def read_thread(ue_ip):
    ws = None
    try:
        ws = create_connection('ws://%s:9002' % ue_ip)
        ws.recv()

        ws.send('{"message":"config_get"}')
        result =  ws.recv()

        j_res = json.loads(result)
        utils.ue_info(ws, j_res, ue_ip)


        ws.close()
        
    except Exception as e:
        print(e)
        print('ue @ %s is not connected !' % ue_ip)
        if ws:
            ws.shutdown


def read(data=None):
    global ue_list
    for ip_i in ue_list:
        threading.Thread(target=read_thread,kwargs=dict(ue_ip=ip_i)).start()


def write(vl, data=None):
    print "(plugin: %s host: %s type: %s pl.i: %s ty.i: %s): %s\n" % (vl.plugin, vl.host, vl.type,vl.plugin_instance,vl.type_instance, vl.values)


def init():
    global ue_list
    print("loading UE list")
    f = open('/etc/collectd/plugins/ue_list.cfg', 'r')
    ue_list = f.read().splitlines()
    print(ue_list)

collectd.register_read(read)
collectd.register_write(write)
collectd.register_init(init)
