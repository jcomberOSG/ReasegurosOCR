import wmi

# c = wmi.WMI("osg-appdf.segurosorion.local", user="jcomber", password="orion.2017")

connection = wmi.connect_server(
  server="osg-appdf.segurosorion.local",
  user="jcomber",
  password="orion.2017")
c = wmi.WMI(wmi=connection)


for os in c.Win32_OperatingSystem():
  print os.Caption
