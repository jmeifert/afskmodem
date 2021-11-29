from nbfmmodem import digitalTransmitter
from nbfmmodem import digitalModulationTypes
transmitter = digitalTransmitter(digitalModulationTypes.default())
print("NBFMmodem TX Demo")
while True:
    print("Enter message string (ASCII):")
    userMessage = input()
    print("Transmitting... Est TX time " + str(transmitter.estTxTime(len(userMessage))) + " seconds.")
    transmitter.tx(userMessage.encode("utf-8"))
    print("Done. (CTRL-C to exit)\n")
