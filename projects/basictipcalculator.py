def start():
  print("wope")

while True:
  print("Welcome to the Tip LOW-CAL CALZONE ZONE Zone Hardcore Ripped Calculator!")
  print("Good = 10% of Bill")
  print("Bad = 5% of Bill")
  dialogue = input("Was your waitress/waitor 'good' or 'bad'? (type 'end' to stop the calculator): ")
  dialogue.lower()

  if dialogue == "good":
    gooddialogue = input("Perfect! Wonderful to hear he/she was good. How much was the bill total? (NO DOLLAR SIGN): ")
    gooddialogue.lower()
    if gooddialogue.isdigit():
      goodbill = int(gooddialogue) * .10
      print("The tip comes out to: $", goodbill)
      print("")
    else:
      print("INVALID INPUT: not an integer")
      print("")

  elif dialogue == "bad":
    baddialogue = input("Welp! Sorry to hear he/she was bad. How much was the bill total?: ")
    baddialogue.lower()
    if baddialogue.isdigit():
      badbill = int(baddialogue) * .05
      print("The tip comes out to: $", badbill)
      print("")

    else:
      print("INVALID INPUT: not an integer")
      print("")


  elif dialogue.isdigit():
    print("INVALID INPUT:  not a valid response (good,bad or end)")
    print("")

  elif dialogue == "end":
    print("I hope you enjoyed the calculator!")
    break

  else:
    print("INVALID INPUT: not a valid response (good,bad or end)")
    print("")
