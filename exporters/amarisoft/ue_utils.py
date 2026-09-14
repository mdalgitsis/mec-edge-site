import collectd  
import json


def ue_info(ws, j_res, ue_ip):
    cells=[] 
    
    vl = collectd.Values(type='count')
    vl.plugin="UE_cells"
    vl.plugin_instance='total'
    vl.host=ue_ip
    vl.interval=5
    if j_res and j_res.get('cells'):
        for key in j_res.get('cells'):
            cells.append(key)

    for cell in cells:
        vl.dispatch(values=[j_res["cells"][cell]['dl_earfcn']])
        
