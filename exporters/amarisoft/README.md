# Amarisoft RAN metrics — per-UE extension

These are the collectd plugins I wrote to add **per-UE monitoring** to the Amarisoft Prometheus exporter,
plus a short guide on how to add further metrics to it.

## Attribution

The exporter itself is **not my work**. It is:

> **[amarisoft-prometheus-exporter-collectd](https://github.com/core-ncsrd/amarisoft-prometheus-exporter-collectd)**
> by Andreas Foteas, NCSR "Demokritos" (MediaNetLab), 2020.

That project builds a collectd daemon with Python plugins that open WebSocket connections to the Amarisoft
EPC (`LTEMME`) and eNB/gNB (`LTEENB`) remote APIs, translate the JSON responses into collectd values, and expose
them to Prometheus through the `write_prometheus` plugin.

Upstream carries **no license file**, so its code is not redistributed here — clone it from the link above.
This directory contains only files I authored, and the deployment work for running it in Kubernetes lives in
[`../../manifests/amarisoft-exporter`](../../manifests/amarisoft-exporter).

## What I added

Upstream collected EPC and eNB statistics. It had no notion of an individual UE, so a per-subscriber view of the
radio link was not available. These plugins add it:

| File | Purpose |
|---|---|
| `ue_stats.py` | collectd plugin: reads `ue_list.cfg`, opens a WebSocket to port 9002 on each UE, issues `config_get`, and dispatches the results on a thread per UE |
| `ue_utils.py` | Translates the UE JSON into collectd values — currently cell count and `dl_earfcn` per cell |
| `ue_list.cfg` | The list of UE addresses to poll |
| `adding-metrics.md` | How to extend any of the exporter's plugins with new metrics: the `collectd.Values()` contract, how `plugin` / `plugin_instance` / `type_instance` / `host` become Prometheus labels, and why every type must exist in `types.db` first |

Alongside these I extended the existing eNB and EPC plugins to collect throughput, MCS, PUSCH/PUCCH SNR and CQI
per connected UE. Those changes are modifications to upstream files rather than new ones, so they are described
in [`../../docs/04-amarisoft-monitoring.md`](../../docs/04-amarisoft-monitoring.md) rather than copied here.

## Installing

Clone upstream, drop these files into `collectd/data/plugins/`, and register the plugin in `collectd.conf`:

```
<Plugin python>
    ModulePath "/etc/collectd/plugins"
    Import "ue_stats"
</Plugin>
```

Every metric type dispatched must already exist in `collectd/data/types.db`, or collectd drops the value and logs
a type error. `adding-metrics.md` covers this.

## Caveats

- **Python 2.** These plugins use `print` statements and were written against the collectd Python plugin of the
  era. They need porting for a Python 3 collectd build.
- `ue_utils.py` currently dispatches `dl_earfcn` under a `count` type — correct for the dashboards it fed, but
  the naming is misleading and would be worth cleaning up.
- The WebSocket port (`9002`) is hardcoded.
