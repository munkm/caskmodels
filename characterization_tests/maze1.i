Maze Variant One
c -------------------------------------------------------------------
c
c              Cell Cards
c
c -------------------------------------------------------------------
1     1  4.96370e-5    1 -2 3 -4 11 -21    imp:n=1 
2     1  4.96370e-5    1 -2 3 -4 26 -41 50 imp:n=1  
c
c     air component of maze
11    1  4.96370e-5    1 -2 31 -32  21 -23 imp:n=1 
12    1  4.96370e-5    1 -2 32 -33  22 -23 imp:n=1 
13    1  4.96370e-5    1 -2 33 -34  22 -25 imp:n=1 
14    1  4.96370e-5    1 -2 35 -33  24 -25 imp:n=1 
15    1  4.96370e-5    1 -2 36 -35  24 -26 imp:n=1 
c
c     solid component of maze
21    2  -1.00         1 -2  3 -31  21 -23 imp:n=1   
22    2  -1.00         1 -2  3 -33  23 -24 imp:n=1 
23    2  -1.00         1 -2  3 -36  24 -26 imp:n=1 
24    2  -1.00         1 -2 32  -4  21 -22 imp:n=1  
25    2  -1.00         1 -2 34  -4  22 -25 imp:n=1 
26    2  -1.00         1 -2 35  -4  25 -26 imp:n=1 
c
c     NaI detector
31    3  -3.67         -50                 imp:n=1 
c
999    0  -1:2:-3:4:-11:41       imp:n=0 

c -------------------------------------------------------------------
c
c              Surface Cards
c
c -------------------------------------------------------------------
c
*1   pz   0
*2   pz   100
*3   py   -50
*4   py    50
c           area behind the source
*11  px   -100                                          $ Back wall 
c
c            maze surfaces
21  px   -50
22  px   -30
23  px   -20
24  px    20
25  px    30
26  px    50
c
31  py    10
32  py    20
33  py    30
34  py    40
35  py   -30
36  py   -40
c             area containing the detector
*41  px    100                                           $ Other back wall
c
c
50  rpp  70 80   0 10  45 55                             $ NaI detector 

c -------------------------------------------------------------------
c
c               Material Cards
c
c -------------------------------------------------------------------
mode n
m1    7014.70c  3.89551e-05  $ air @ 293.6K
      7015.70c  1.43884e-07  $ total = 4.96370e-05
      8016.70c  1.05340e-05
      8017.70c  4.01267e-09
c
m2   1001.70c -.114   $ Li-doped polyethylene
     8016.70c -.399   $ density = 1.0 g/cc
     6000.70c -.474
     3006.70c -0.000949
     3007.70c -.012051
c
c m3    92235.70c .90          $ 90% enriched UO2
c      92238.70c .10          $ density = 10.97 g/cc
c      8016.70c  2.0
c
c       sodium iodide        3.67 g/cc
m3    11023.70c -0.1534       $ Na =  22.989770
      53127.70c -0.8466       $ I  = 126.904470
c
c
sdef POS -75.0 0.0 50.0 PAR=1 ERG=10.0  
c
c      tally for fw-CADIS method
fmesh24:n origin -100 -50 0
         imesh -50 50 100
         jmesh 50  
         kmesh 40 60 100
         iints 50 200 50
         jints 100
         kints 20 20 20
c
c       tally for CADIS method
f44:n   31
e44     10e-8 8I 10e-7 8I 10e-6 8I 10e-5 8I 10e-4 8I 10e-3
c
nps 1000000
print
