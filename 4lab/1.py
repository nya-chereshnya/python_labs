import math


class PacketDataTransmission:
    def __init__(self, messageSize, packetSize):
        self.__messageSize = self.__convertSizeInBytes(messageSize)
        self.__packetSize = self.__wrongValueCheck(
            self.__convertSizeInBytes(packetSize))

    def __wrongValueCheck(self, dataSize):
        if dataSize < 32 or dataSize > 32 * 1024:
            print("wrong data size")
            return 0
        return int(dataSize)

    def __convertSizeInBytes(self, dataSize):
        try:
            if "KB" in dataSize or "kb" in dataSize:
                return int(float(dataSize[:-2]) * 1024)
            elif "MB" in dataSize or "mb" in dataSize:
                return int(float(dataSize[:-2]) * 1024 * 1024)
            elif "GB" in dataSize or "gb" in dataSize:
                return int(float(dataSize[:-2]) * 1024 * 1024 * 1024)
            else:
                return int(dataSize)
        except Exception as e:
            print("wrong input type,", e, end="")
            return 0

    @property
    def messageSize(self):
        return self.__messageSize

    @property
    def packetSize(self):
        return self.__packetSize

    @packetSize.setter
    def packetSize(self, packetSize):
        self.__packetSize = self.__wrongValueCheck(
            self.__convertSizeInBytes(packetSize))

    def getPacketsNumber(self):
        try:
            return math.ceil(self.__messageSize / self.__packetSize)
        except ZeroDivisionError:
            print("wrong packet size, unable to determine the number of packets")
            return 0


lol = PacketDataTransmission("34051", "3KB")
# print(lol.packetSize)
# lol.packetSize = "3KB"
print("packet size ", lol.packetSize)
print("message size ", lol.messageSize)
print("packets number ", lol.getPacketsNumber())
