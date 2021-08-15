#! /bin/bash

dwm_weather(){

DATA=$(python /home/phill/software/dwm-bar/bar-functions/weather_rhmz.py)
export __DWM_BAR_WEATHER__="${SEP1} ${DATA}${SEP2}"
}

dwm_weather
