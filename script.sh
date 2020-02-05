#!/bin/bash
kill $(lsof -t -i:$3)
cd /root/$1/
rm -rf env
#!virtualenv --python=/usr/bin/${10} env
${4} -m venv env
source env/bin/activate
cd /root/$1/einvoice-app-falcon
pip install -r requirements.txt
echo "gunicorn --worker-class=gevent --worker-connections=1000 --workers=15 -b $2:$3 --timeout 1800 main:APP --error-logfile /root/einvoice-falcon-dev/error.log --access-logfile /root/einvoice-falcon-dev/access.log --reload >> /root/einvoice-falcon-dev/einvoice-app-falcon/falcon_einvoice_api.log &"
/root/$1/env/bin/gunicorn --worker-class=gevent --worker-connections=1000 --workers=15 -b $2:$3 --timeout 300 main:APP --error-logfile /root/einvoice-falcon-dev/error.log --access-logfile /root/einvoice-falcon-dev/access.log --reload >> /root/einvoice-falcon-dev/einvoice-app-falcon/falcon_einvoice_api.log &
sleep 15s
val=`lsof -t -i:$3 | wc -l`
echo $val
if [ $val == "16" ];
then
        echo "E-INVOICE Service has been deployed successfully"
else
        echo "E-INVOICE Service deployment has been failed"
		exit 1
fi
