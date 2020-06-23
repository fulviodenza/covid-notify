try:
    import notify2
except ImportError:
    print("run pip install notify2")
import json
import urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def notify():
    url_today = urllib.request.urlopen(
        "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json")
    url_yesterday = urllib.request.urlopen(
        "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
    )

    data_today = json.loads(url_today.read())
    data_yesterday = json.loads(url_yesterday.read())
    yesterday_index = len(data_yesterday)
    notify2.init("covid-info")

    variazione_deceduti = int(data_today[0]["deceduti"]) - int(data_yesterday[yesterday_index-2]["deceduti"])
    variazione_guariti = int(data_today[0]["dimessi_guariti"]) - int(data_yesterday[yesterday_index-2]["dimessi_guariti"])

    msg = "POSITIVI: {} (+{}) di cui {} ({}) attuali DECEDUTI: {} (+{}); GUARITI: {} (+{})".format(
        data_today[0]["totale_casi"], data_today[0]["nuovi_positivi"], 
        data_today[0]["totale_positivi"], data_today[0]["variazione_totale_positivi"], 
        data_today[0]["deceduti"], 
        variazione_deceduti, data_today[0]["dimessi_guariti"], variazione_guariti
        )

    n = notify2.Notification("Covid today",
                            msg,
                            "notification-message-im"   # Icon name
                            )
    n.timeout = 10000
    n.show()


scheduler.add_job(notify, 'interval', hours=1)
scheduler.start()