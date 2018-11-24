import yaml,os
def read_yaml():
    with open(os.getcwd()+os.sep+"Data"+os.sep+"login_data.yaml","r",encoding="utf-8") as f:
        print(yaml.load(f))
        return yaml.load(f)

if __name__ == '__main__':
   read_yaml()