<h1>Scripts for running and profiling the TUM quadcopter/SLAM simulation</h1>

<h2>Running</h2>

```
bash run_autopilot.bash
```

<h2>Scripts</h2>
The sendFlightPlan.bash script will send flight plans like the ones in the TUM repositories flightPlans directory. However, it assumes the flight plans don't have blank lines.
The GUI client automatically sends the command to start the autopilot, so the flightPlans in the TUM will not work directly currently. 


<h3>Notes</h3>
The state estimation node is fragile, and prone to crashing if it fails to find sufficient features. There is some matrix decomposition happening that fails an assertion in this case. 

