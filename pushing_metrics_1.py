from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge('my_metric', 'Help text', registry=registry)
g.set_to_current_time()
push_to_gateway('localhost:9182', job='my_job', registry=registry)