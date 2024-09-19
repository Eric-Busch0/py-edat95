"""Implementation for EmbEdat
"""

from enum import Enum
from typing import Tuple
import hid


CMD_OPT_GET_NAME = 0
CMD_OPT_GET_ATTENUATION = 1
CMD_OPT_SET_ATTENUATION = 2


class CommandOption(Enum):
    GET_NAME = 0
    GET_ATTENUATION = 1
    SET_ATTENUATION = 2
    SET_INSERTION_LOSS = 3
    GET_INSERTION_LOSS = 4
    GET_FAULT_STATUS = 5
    CLEAR_FAULTS = 6


class CmdStatus(Enum):
    OK = 0
    BAD_ATTENUATION = 1
    FAIL = 0xFF


class CmdStatusError(Exception):
    pass


class Edat95:
    """EMB Electronic Digital Attenuator"""

    VID = 0x483
    PID = 22352

    def __init__(self, serial: int = None) -> None:
        self.dev = hid.device()
        self.dev.open(self.VID, self.PID, serial_number=serial)

    def _write(self, cmd: CommandOption, data=None):

        if data and len(data) > 63:
            raise AttributeError("Length of daata can only be up to 63")

        tx_buf = [0] * 64
        tx_buf[0] = cmd.value
        if data:
            for i, datum in enumerate(data):
                tx_buf[i + 1] = datum
        tx_buf = bytes(tx_buf)
        self.dev.write(tx_buf)

        resp = self.dev.read(64)
        err = CmdStatus(int(resp[0]))

        if err != CmdStatus.OK:
            raise CmdStatusError(f"Command failed: {err} {resp}")

        return resp[1:]

    def get_serial_number(self) -> str:
        """Get serial number

        Returns:
            str: serial number
        """
        return self.dev.serial

    def get_name(self) -> Tuple[int, str]:
        """Get Name of device

        Returns:
            str: Name of device
        """

        resp = self._write(CommandOption.GET_NAME)
        length = resp.index(0)
        return ''.join([chr(i) for i in resp[:length]])

    def get_attenuation(self) -> int:
        """Get current set attenuation

        Returns:
            float: Attenuation in dB
        """

        resp = self._write(CommandOption.GET_ATTENUATION)

        return int(resp[0])

    def set_attenuation(self, attenuation: int):
        """Set attenuation

        Args:
            attenuation (float): attenuation in dB (0 - 31.5)

        Raises:
            ValueError: If attenuation not within 0 - 31.5 dB

        Returns:
            _type_: _description_
        """

        if attenuation > 95:
            raise ValueError("Attenuation may not exceed 95")

        data = [attenuation]

        self._write(CommandOption.SET_ATTENUATION, data)

    def set_insertion_loss(self, loss, store_non_volatile=False) -> int:

        if loss < 0 or loss > 255:
            raise ValueError("Loss is a positive value between 0 and 255")

        self._write(CommandOption.SET_INSERTION_LOSS, [loss, int(store_non_volatile)])

    def get_insertion_loss(self, data) -> int:
        resp = self._write(CommandOption.GET_INSERTION_LOSS)
        return resp[0]
