pemStr = ''
with open("testPemFile.pem","r") as f:
  lines = f.read().splitlines()
  for l in lines:
    pemStr = pemStr+l+'\\n'
print(pemStr)
