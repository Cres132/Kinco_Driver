import sys
import sqlite3
import time
import serial
from pymodbus.client.sync import ModbusSerialClient as modbusclient
from pymodbus.constants import Defaults


class Homing:
    Home_offset = ''
    Homing_method = ''
    Homing_speed_swtitch = ''
    Homing_speed_zero = ''
    Homing_power_on = ''
    Homing_acceleration = ''
    Homing_current = ''
    Defaults.RetryOnEmpty = True
    Defaults.Timeout = 5
    Defaults.Retries = 5
    def standard_homing():

        client = modbusclient(method='RTU', port='/dev/ttyUSB0', timeout=1, stopbits=1, bytesize=8, parity='N', baudrate=19200)
        connectResult = client.connect()



        try:
            rq = client.write_register(address=0x3100, value=0x0F, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x3100, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x3100, value=0x0F, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x3100, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            rq = client.write_register(address=0x3500, value=6, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x3500, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x3500 , value=6, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x3500 , count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")


        try:
            rq = client.write_register(address=0x4100, value=0, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x4100, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x4100, value=0, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x4100, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")



        try:
            rq = client.write_register(address=0x4D00, value=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x4D00, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x4D00, value=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x4D00, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5010, value=100, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x5010, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5010, value=100, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x5010, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5020, value=100, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x5020, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5020, value=100, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x5020, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5020, value=100, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x5020, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5020, value=100, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x5020, count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")


        try:
            rq = client.write_register(address=0x5200, value=50, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            hh = client.read_holding_registers(address=0x5200, count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x5200, value=0x0F, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x3100 , count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:
            hh = client.read_holding_registers(address=0x3100 , count=1, unit=1)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")

        try:
            rq = client.write_register(address=0x3100 , value=0x0F, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        try:

            hh = client.read_holding_registers(address=0x3100 , count=1, unit=2)
            assert (hh.function_code < 0x80)
            print(str(hh))
        except default:
            print("error")
        client.close()
