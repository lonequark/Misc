# PROGRAM TITLE
# Want to make a calculator for straight track airtime hills. Input speed, desired g force, and force change rate. Find best profile for airtime.
# Last Updated: MM/DD/YEAR
#
# Changelog:
# Version 1.0
#	- MM/DD/YY: Initial Release.
#
#


# Inputs:
speed = 20 #m/s
maxGForce = 3.5 #g
minGForce = 0 #g
changeRate = 3 #g/sec

# Quick conversions
maxGForce = 9.81*(maxGFforce-1) # Shifts frame of reference, converts to m/s**2
minGForce = 9.81*(minGForce-1) # Ditto
changerate = 9.81*changerate # Converts to m/s**2, no need for shift

# Current state:
force = 1
pitch = 0