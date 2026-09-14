# Add metrics

### In <element>_utils.py

In .../amarisoft-prometheus-exporter-collectd/collectd/data/plugins/

The functions must have

```
def <function_name>(j_res,...):
    .
    .
    <funciton actions>
    .
    .
    vl = collectd.Values(type='<type>')  # This <type> must be in the DB (type.db in .../amarisoft-prometheus-exporter-collectd/collectd/data/)
    vl.plugin='<plugin_name>' # This <plugin_name> is the name of the metric --> colled_<plugin>_<type>
    vl.plugin_instance='<plugin_instance_name>' # This <plugin_instance_name> is an extra label for the target/metric --> <plugin>=<plugin_instance>
    vl.type_instance='<type_instance>' # This <type_instance> is an extra label for the target/metric --> type=<type_instance>
    vl.host=<host> # This <host> is an extra label for the target/metric --> exported_instance=<host>
    vl.interval=<interval> ## For ecample vl.interval=5
    
    vl.dispatch(values=[j_res[...]]) # These are the values of the metrics (the same number of values as the type (ul_freq) has in DB)


```

***The colletc.Values(), plugin, interval and dispatch are mandatory,*** the rest are optional as extra labels

### In <element>_stats.py

In .../amarisoft-prometheus-exporter-collectd/collectd/data/plugins/


Add the functions after the query of json

```
utils.<function_name>(j_res,...)
```

### In type.db

In .../amarisoft-prometheus-exporter-collectd/collectd/data/

Add the types used in the <element>_utils.py

```
<type>                 <extra_label>:GAUGE:0:U
```

***The extra_label could be "value" if you do not want any extra label***



### Metric in prometheus

The name of the metric should be 

	<job_name>_<plugin>_<type>_<extra_label>

example

	job=collectd
	plugin=freq
	type=ul_freq
	extra_label=FREQ

	Metric=collectd_freq_ul_freq_FREQ

If extra_label=value

	Metric=collectd_freq_ul_freq


and the result of the prometheus query should be

        <job_name>_<plugin>_<type>_<extra_label>{exported_instance="<host>",<plugin>="<pluging_instnce>",instance="localhost:9103",job="<job_name>",type="<type_instance>"}

example

        job=collectd
        plugin=freq
        type=ul_freq
        extra_label=FREQ
	pluging_instnce=ul
	type_instance=nr
	host=ran_id=74565


	collectd_freq_ul_freq_FREQ{exported_instance="74565",freq="ul",instance="localhost:9103",job="collectd",type="nr"}
