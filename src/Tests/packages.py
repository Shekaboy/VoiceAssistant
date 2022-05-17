#Check if all package dependencies are present 
#If they are absent install them 
import pkg_resources
import sys
import subprocess

sys.path.append("..")
from src.Utils.comm import Message 


class CheckRequirements:
  def __init__(self,path) -> None:
      with open(path,'rb') as f:
        contents = f.read()
        contents = contents.decode("ISO-8859-1")
        contents = contents.split("\r\n")
        self.dependencies = list(filter(None, contents))
      self.pat = path

  def check_requirements(self) ->Message:
    try:
      pkg_resources.require(self.dependencies)
    except Exception as e:
      return Message(False,"Requirements not installed",e) 
    return Message(True,"","") 
  def install_requirements(self)->Message:
    try:
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r',self.pat])
      subprocess.check_call([sys.executable, 'pipwin', 'install', 'pyaudio'])
      reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
      installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
      return Message(True,installed_packages,"") 
    except Exception as e:
      return Message(False,"Unable to install packages",e)


if __name__ == "__main__":
  cr = CheckRequirements("requirements.txt")
  print(cr.check_requirements().value)
  print(cr.install_requirements().value)
