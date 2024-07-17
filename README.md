# XHbbYttbar

# Step 1: Getting MC and data files:

```
python raw_nano/get_data.py
python raw_nano/get_MC.py
```

# Step 2: Generate snapshots

```
python snapshot.py -s <setname> -y <year> -j <job#> -n <njobs>
```
will run a snapshot on the `j`th job out of a total `n` number of jobs
