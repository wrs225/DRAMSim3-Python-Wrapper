# DRAMSim3-Python-Wrapper

This repo creates a DRAMsim python wrapper. Everything is built with a makefile. Just go into the repo and run

```
  cd DRAMsimWrapper
  make
```

This should add a bunch of garbage files to your DRAMsimWrapper folder. You should now be able to run any of the Python tests. The makefile is configured to test the Python wrapper implementation to make sure it does not immediately crash python. 

```
  cd ../
  python <any_of_the_provided_tests.py>
```

You can also borrow more Memory Configs from DRAMSim3 and add them to the MemoryConfigs folder to use other memory models. 

The version of DRAMsim3 used to compile this code is included in this Github Repository. 

```
  make clean
```
will remove any of the built files in DRAMsimWrapper
