import subprocess
import sys

from pip._internal.utils.misc import get_installed_distributions


class PreRequisits:
    check = True

    def install(self, package):
        print("Installing the package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

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
            print(f"{package_to_install} already in site-packages")
        else:
            print(f"{package_to_install} is not installed")
            self.install(self, package_to_install)


text = PreRequisits()
text.installing_prerequisites("PyAutoGUI")
