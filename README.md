# redis-cli_exporter
prometheus, rediscli_exporter
需要安装 prometheus_client，flask，redis 等模块。
pip install prometheus_client ；
pip install flask  ；
pip install redis  ；
用Flask web框架写的，类似于zabbix上面对 Redis的某个队列（list）长度进行监控，获取到长度之，吐到 /metrics， 供Prometheus调用。




OK，that is all.
