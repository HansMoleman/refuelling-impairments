# refuelling-impairments
**Created:**&nbsp;&nbsp; October 25<sup>th</sup>, 2025  
**Updated:**&nbsp; 10-25-2025 @ 8:32 PM  

A tool for monitoring and analyzing system hardware usage while running iRacing.

---

### Index of Contents

1. [State of System](#state-of-system)
2. [Objectives](#objectives)
3. [Notes](#notes)

---

<br>

## 1 &nbsp;&nbsp; State of System

The following is a summary of the system's current state:

...


<br>

## 2 &nbsp;&nbsp; Objectives

- [ ] implement ability to monitor CPU usage on a set interval
- [ ] implement ability to record CPU usage as it monitors it on a set interval
- [ ] implement ability to monitor and record RAM usage on a set interval
- [ ] implement ability to monitor and record disk read/write usage on a set interval
- [ ] give user ability to both run and stop system at will
- [ ] implement ability to produce graph of CPU usage
- [ ] implement ability to save image of CPU usage graph to disk


<br>

## 3 &nbsp;&nbsp; Notes

10-25-2025  

Algorithm for the main use case:

* user starts monitoring tool before loading sim session.
* system initializes.
* system begins monitoring target hardware/computer resources and records necessary data on a set interval until user interrupts it.
* user interrupts the system.
* system stops monitoring/recording.
* system reads back data it has recorded and uses it to create graphical plots representing it.
* system saves created plots as images and then deletes all recorded data.
* system exits.


<br>
<br>
<br>
<br>

---

<br>
<br>
