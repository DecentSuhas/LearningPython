import subprocess
import time


def start_adb_log(device_serial, iteration):
    """
    To start adb log
    :param device_serial: Device Serial Number
    """
    cmd = "adb -s " + device_serial + " logcat -v time>automation_trial_"+iteration+".txt"
    subprocess.call(cmd, shell=True)
    print("Starting the adb log...")
    time.sleep(5)


def stop_adb_logging():
    cmd = "adb shell killall -2 logcat"
    subprocess.call(cmd, shell=True)
    print("Stopped the adb log...")


#  For Lumea
def start_adb_log(self, scenario):
    """
        Start adb log
    :param self:
    :param scenario:
    :return:
    """
    device_serial = self.serial_number
    name = scenario
    testcase_name = str(name)
    testcase_name1 = testcase_name[10:20]
    cmd = "adb -s " + device_serial + " logcat -d -v time>" + testcase_name1 + ".txt"
    subprocess.call(cmd, shell=True)
    print("Starting the adb log...")


@staticmethod
def stop_adb_logging():
    """
        To stop all adb logcat
    :return:
    """
    cmd = "adb shell killall -2 logcat"
    subprocess.call(cmd, shell=True)
    print("Stopped the adb log...")


def before_scenario(context, scenario):
    """This function will set up requirements before every test case executes"""
    context.utilities.start_adb_log(scenario)