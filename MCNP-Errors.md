This page contains information on errors that were thrown while trying to run MCNP on savio and their solutions (or at least what we did to stop getting the error).

### Cross-Section errors
* While first trying to run MCNP, we were getting errors while trying to load cross-sections. Below is the error we would get:

```
 bad trouble in subroutine ffetch of xact                             

 cannot find xs library file specified in xsdir  
```

* This was due to the default DATAPATH variable leading to an xsdir directory that was missing one of the cross-section libraries.
* This error was resolved by changing the DATAPATH variable to a correct xsdir path that contains all the needed xs libraries.

***

### Segmentation Faults
* This was an error that would be thrown about 1 hour into an MCNP run and would cause the run to fail. Below is the error that was printed to the slurm.err file:

```
forrtl: severe (174): SIGSEGV, segmentation fault occurred
Image              PC                Routine            Line        Source
mcnp5.mpi          000000000073D9B9  Unknown               Unknown  Unknown
mcnp5.mpi          000000000073C28E  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000664172  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000616DA8  Unknown               Unknown  Unknown
mcnp5.mpi          000000000061FE0B  Unknown               Unknown  Unknown
libpthread.so.0    00002BA87B2FE710  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000508F93  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000588C9F  Unknown               Unknown  Unknown
mcnp5.mpi          00000000004A7985  Unknown               Unknown  Unknown
mcnp5.mpi          00000000005A6D3C  Unknown               Unknown  Unknown
mcnp5.mpi          00000000005063CF  Unknown               Unknown  Unknown
mcnp5.mpi          00000000004D55BB  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000438716  Unknown               Unknown  Unknown
libc.so.6          00002BA87B52AD5D  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000438609  Unknown               Unknown  Unknown
forrtl: error (78): process killed (SIGTERM)
Image              PC                Routine            Line        Source
mcnp5.mpi          000000000073D9B9  Unknown               Unknown  Unknown
mcnp5.mpi          000000000073C28E  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000664172  Unknown               Unknown  Unknown
mcnp5.mpi          0000000000616DA8  Unknown               Unknown  Unknown
...
```

* This error was resolved by using the "prdmp" MCNP card. The following card was used:
```
prdmp 4j -1
```

* This card makes MCNP particle rendezvous and dumps to the runtpe file more frequent.
* I believe the segmentation fault was caused due to the nodes running out of system memory before it was scheduled to dump to the runtpe file. This card causes the dumps to occur more frequently, which prevent the system from reaching the memory limit.



