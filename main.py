from garmin_fit_sdk import Decoder, Stream
import sys

# garminInterface is a simple class used to write the contents of a garmin .fit file
# into a text file, as readable data. further data formatting and CLA's are viable strategies for
# improvement


class garminInterface:
    # writeToFile takes an output file name and a fit file, and puts the valuable data to the output file from the .fit file
    def writeToFile(self, fitFileName: str, fileName: str) -> None:
        # Getting the data from the file in the form of binary
        stream = Stream.from_file(fitFileName)
        decoder = Decoder(stream)
        # Callign the Garmin SDK API to decode the binary into a dictionary data structure
        messages, errors = decoder.read()

        # if the .fit file was properly converted
        if errors == []:
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open(fileName, 'w') as f:
                # Change the standard output to the file we created.
                sys.stdout = f
                print(messages.get("session_mesgs"))
                sys.stdout = original_stdout  # Reset the standard output to its original value
        else:
            print(errors)


# writing the data to an output file
obj = garminInterface()
obj.writeToFile("16001776188_ACTIVITY.fit", "output.txt")
