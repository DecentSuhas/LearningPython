# Developed by: Suhas KS

import subprocess
import sys
import time
import os
from pip._internal.utils.misc import get_installed_distributions


class PreRequisits:
    check = True
    def install(self, package):
        print("Installing the package. Please wait...")
        os.system('pip install '+package)
        time.sleep(60)

    def findPackage(self, package_name):
        packages = []
        global check
        for i in get_installed_distributions(local_only=True):
            text1 = str(i)
            packages.append(text1)
        for k in packages:
            if package_name in k:
                check = True
                break
            else:
                check = False
        return check

    def installing_prerequisites(self, package_to_install):
        is_installed = self.findPackage(package_to_install)
        if check:
            print(f"{package_to_install} is already installed.")
        else:
            print(f"{package_to_install} is not installed.")
            self.install(package_to_install)


text = PreRequisits()
text.installing_prerequisites("PyAutoGUI")
text.installing_prerequisites("Pillow")
text.installing_prerequisites("opencv-python")
