FROM debian:bookworm

# Installa gli strumenti necessari: rsyslog per il logging, curl per le richieste,
# filebeat per l'invio centralizzato dei log (oppure installa una versione compatibile)
RUN apt-get update && apt-get install -y \
    rsyslog \
    curl \
    filebeat \
    && rm -rf /var/lib/apt/lists/*

# Copia la configurazione di Filebeat nel container
COPY filebeat.yml /etc/filebeat/filebeat.yml

# Copia l'entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# L'entrypoint avvia il container con i comportamenti e Filebeat
ENTRYPOINT ["/entrypoint.sh"]
