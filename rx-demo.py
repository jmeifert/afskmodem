from nbfmmodem import digitalReceiver
from nbfmmodem import digitalModulationTypes
receiver = digitalReceiver(digitalModulationTypes.bpsk500())
while(True):
    print("Waiting for message...\n")
    print(receiver.rx())
    print("\nDone. (CTRL-C to exit)")