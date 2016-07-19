# Simulate the following situation.  At a post office, customers enter a single line waiting to be served by any one of two clerks.
# Every minute there is a 60% chance that a new customer arrives.  If there is no one in line and a server is free, the customer does
# not wait to be served.  When a customer is being served there is a 25% chance every minute that they complete their business and
# leave.  When the clerk is free he will take the next customer in line, in the order that they arrived.  Every minute, there is
# a 5% chance that a person standing in line will give up and leave.  The post office is always open(24/7/365).  For simplicity you
# can assume customers will always arrive at the beginning of the minute and if they leave they do so at the end of the minute.  
# a.] What is the average amount of time a customer spends in the post office (including not being served)?
# b.] What percentage of customers leave without being served?
# c.] What percentage of the time are the clerks idle?


#initalizations 
import random



def postOffice(mins):
  l1 = []
  l2 = []
  totalMins = 0.0
  totalCust = 0.0
  notServed = 0.0
  idleTime = 0.0

  for i in range(0, mins):
    for j in range(0, len(l1) - 1):
      l1[j] += 1
    for h in range(0, len(l2) - 1):
      l2[h] += 1

    # calculates the amount of time each clerk is idle
    if len(l1) == 0:
      idleTime += 1
    if len(l2) == 0:
      idleTime += 1
    
    #every minute there is a 60% chance a new customer arrives
    if random.random() <= .6:
      totalCust += 1 
      if len(l1) < len(l2):
        l1.append(0)
      else:
        l2.append(0)

    #every minute there is a 25% chance the customer will complete their business and leave
    if len(l1) != 0:
      if random.random() <= .25:
        totalMins += l1[0]
        del l1[0]

    if len(l2) != 0:
      if random.random() <= .25:
        totalMins += l2[0]
        del l2[0]

    #every minute there is a 5% chance the customer will give up and leave
    if len(l1) > 1:
      for j in range(1, len(l1) - 1):
        if random.random() <= .05:
          notServed += 1
          if j >= len(l1):
            break
          totalMins += l1[j]
          del l1[j]
          j -= 1

    if len(l2) > 1:
      for j in range(1, len(l2) - 1):
        if random.random() <= .05:
          notServed += 1
          if j >= len(l2):
            break
          totalMins += l2[j]
          del l2[j]
          j -= 1
 
  return "a.) Average amount of time a customer spends in the post office: " + str(totalMins / totalCust) + "\n b.) Percentage of customers that leave without being served: " + str(notServed / totalCust * 100) + "\n c.) Percentage of time the clerks are idle: " + str(idleTime / totalMins * 100)



print(postOffice(365 * 24 * 60))


