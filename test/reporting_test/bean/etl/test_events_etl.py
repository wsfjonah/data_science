import reporting.bean.etl.events_etl as events_etl

events_etl = events_etl.EventsETL('WSN Event Statistics by Hour', 'Hour', 'Magnitude')
events_etl.draw()
