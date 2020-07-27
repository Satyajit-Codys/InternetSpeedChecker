import speedtest
s= speedtest.Speedtest()
servers =[]
s.get_servers(servers)
s.get_best_server()

print("Ping Speed: " + str(s.results.ping) + "  MS")
print("Download Speed: "+ str(s.download()//1048576) + " MBits/Second")
print("Upload Speed: "+ str(s.upload()//1048576) + " MBits/Second")
