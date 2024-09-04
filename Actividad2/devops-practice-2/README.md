### DevSecOps integration

1. Security analisis tool configured

```bash
npm audit
```

2. Add this command into github actions script

```bash
- name: Run security script
  run: npm audit
```

3. Configure prometheus and grafana to start monitoring the app.
3.1. Create a prometheus.yml fil

```bash
global:
	scrape_interval: 15s

scrape_configs:
	- job_name: 'node-app'
	  static_configs:
	   - targets: ['app:3000']
```

3.2. Modify the docker compose file and add:

```bash
prometheus: 
	image: prom/prometheus 
	volumes: 
		- ./prometheus.yml:/etc/prometheus/prometheus.yml 
	ports: 
		- "9090:9090"
```

```bash
grafana:
	image: grafana/grafana
	ports:
		- "3001:3001"
```


