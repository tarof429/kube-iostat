#!/usr/bin/python


from flask import Flask, jsonify, request
import psutil
import json

app = Flask(__name__)

@app.route('/cputimes')
def get_cpu_times():

    times = psutil.cpu_times()

    ret = {}
    ret['user'] = times.user
    ret['nice'] = times.nice
    ret['system'] = times.system
    ret['idle'] = times.idle
    ret['iowait'] = times.iowait
    ret['irq'] = times.irq
    ret['softirq'] = times.softirq
    ret['steal'] = times.steal
    ret['guest'] = times.guest
    ret['guest_nice'] = times.guest_nice

    return json.dumps(ret)


@app.route('/cpupercent')
def get_cpu_percent():
    p = psutil.cpu_percent(percpu=True)

    ret = {}
    ret['value'] = p

    return json.dumps(ret)

@app.route('/cpucount')
def get_cpu_count():
    p = psutil.cpu_count()

    ret = {}
    ret['value'] = p

    return json.dumps(ret)

@app.route('/hello')
def hello_world():
    return 'Hello!\n'
    
if __name__ == '__main__':
    app.run()

