
trap "kill 0" EXIT
clear
echo "PID $$"
echo "Setting up Things....."

sleep 2
echo "-------------------------------------------"
echo "ACTIVATING VIRTUAL ENV"
source ~/venv/temp_imper3.6/bin/activate
p1=$!
if [[ $? == 0 ]]
then
echo "Virtual Envoironment Activated Successfully....."
else
echo "Error while starting Virtual Envoironment"
fi

sleep 5
echo "-------------------------------------------"
echo "Starting Django server"
python /home/xyz/practice/django/crud_operation_project_2/manage.py runserver >> /home/xyz/practice/django/crud_operation_project_2/logs/server_stdout.log 2>>/home/xyz/practice/django/crud_operation_project_2/logs/server_stderr.log &
###python /home/xyz/practice/django/crud_operation_project_2/manage.py runserver & 
p2=$!
if [[ $? == 0 ]]
then
echo "Django Server started Successfully....."
else
echo "Error while starting Django Server...."
fi

sleep 5
echo "-------------------------------------------"
echo "Starting PyWebView"
python /home/xyz/practice/py_web_view/first_eg.py >> /home/xyz/practice/py_web_view/logs/py_web_view.log 2>&1 &
p3=$!
if [[ $? == 0 ]]
then
echo "WebView started Successfully....."
else
echo "Error while starting Webview...."
fi

sleep 5
clear
echo "-------------------------------------------"
echo "Starting Subscriber"
python MqttOperations.py

wait $p1 $p2 $p3
