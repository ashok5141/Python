friends = ["Ashok","Bob","Anne","kumar","Ram"]
time_since_seen = [27,17,7,0,1]

#long_timers = dict(zip(friends, time_since_seen, (1,2,3,4,5,6))) the DICTIONARY throw an error if use the inside the lsit
#long_timers = zip(friends, time_since_seen) throw an error
long_timers = list(zip(friends,time_since_seen,[1,2,3,4,5,6])) # if number inside list is not equal

print(long_timers)