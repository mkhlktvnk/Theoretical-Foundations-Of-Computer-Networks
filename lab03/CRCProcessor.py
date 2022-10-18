class CRCProcessor:
    def crc_16(self, data: str, poly: hex = 0xA001):
        crc = 0xFFFF
        for i in range(0, len(data), 2):
            crc ^= int(data[i:i + 2], 16)
            for _ in range(8):
                crc = ((crc >> 1) ^ poly if (crc & 0x0001) else crc >> 1)
        return hex(crc)[2:].rjust(4, '0')  # Контрольная сумма должна быть 2 байта т.е. 4 символа
