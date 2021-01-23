#!/bin/bash
curl --header "Content-Type: application/json" --request POST --data '{"array":"[1,4,5,2,3, [7,6], 8]"}' http://localhost:5000/api/bubbleSort
curl --header "Content-Type: application/json" --request POST --data '{"array":"[6,2,[4,3],[[[5],7], 1]]"}' http://localhost:5000/api/bubbleSort
curl --header "Content-Type: application/json" --request POST --data '{"array":"[[6,2,[4,3],[[5,8],7], 1]]"}' http://localhost:5000/api/bubbleSort