#!/bin/bash
MAX=1000

for (( i = 0; i < MAX ; i ++ ))
do
    echo $i
    #res=`expr $i % 2`
    #if [ "$res" = "0" ]
    #then
#	./cansend can0 -i 0x123 -e 0x07 0x22 0x33 0x44 0x55 0x66 0x77 0x88
#    else
#	./cansend can0 -i 0x123 -e 0x0a 0x22 0x33 0x44 0x55 0x66 0x77 0x88
#    fi
   
    ./cansend can0 -i 0x01  0x0a 0x01 0x00 0x00 0x00 0x00 0x00 0x00
    sleep 0.01
    ./cansend can0 -i 0x02  0x0a 0x00 0x00 0x00 0x00 0x00 0x00 0x00
    sleep 0.01
    if [ $i -eq 998 ]
    then
        i=0
    fi
done
