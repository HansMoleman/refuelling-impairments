# refuelling-impairments
**Created:**&nbsp;&nbsp; October 25<sup>th</sup>, 2025  
**Updated:**&nbsp; 11-19-2025 @ 8:00 PM  

A tool for monitoring and analyzing system hardware usage while running iRacing.

---

### Index of Contents

1. [State of System](#1--state-of-system)
2. [Objectives](#2--objectives)
3. [Notes](#3--notes)

---

<br>

## 1 &nbsp;&nbsp; State of System

The following is a summary of the system's current state:

* system will fetch CPU and RAM usage data, print it to the display, and then sleep for _n_ seconds.
* system will also print the time offset at which a check occurs.
* system will write the time and value of CPU usage to a .csv data file for each check.
* system starts monitoring/recording process when user starts system, and continues the process until user kills the system (i.e., with CRTL+C).
* system will check for existence of data file from previous session and remove it prior to new data collection.

In Progress:


<br>

## 2 &nbsp;&nbsp; Objectives

- [x] implement ability to monitor CPU usage every _n_ seconds on an infinite cycle
- [x] implement ability to record CPU usage as it monitors it on an infinite cycle
- [x] implement ability to monitor and record RAM usage on infinite cycle
- [ ] implement ability to monitor and record disk read/write usage on infinite cycle
- [x] give user ability to both run and stop system at will
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
